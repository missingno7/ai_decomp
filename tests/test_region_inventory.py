import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from region_inventory import interval_coverage, source_regions, machine_regions


class RegionInventoryTests(unittest.TestCase):
    def test_noncontiguous_coverage_keeps_gaps_and_overlap(self):
        result = interval_coverage([(0, 3), (7, 10), (8, 12)], 15)
        self.assertEqual(result['covered_bytes'], 8)
        self.assertEqual(result['gaps'], [[3, 7], [12, 15]])
        self.assertEqual(result['overlap_bytes_counted_with_multiplicity'], 2)

    def test_bad_machine_extent_is_rejected(self):
        for spans in [[(-1, 2)], [(3, 2)], [(0, 11)]]:
            with self.assertRaises(ValueError):
                interval_coverage(spans, 10)

    def test_source_lines_never_become_machine_membership(self):
        result = source_regions('f', {'A': [2, 4], 'B': [7, 9]}, 10)
        self.assertEqual(result[0]['line_count'], 3)
        self.assertIsNone(result[0]['machine_membership'])
        self.assertIsNone(result[0]['live_outs'])
        with self.assertRaises(ValueError):
            source_regions('f', {'A': [2, 4], 'B': [4, 6]}, 10)

    def test_stale_sidecar_cannot_fit_a_shorter_body(self):
        with self.assertRaisesRegex(ValueError, 'outside retained merged body'):
            source_regions('draw_frame', {'D4': [478, 586]}, 545)

    def test_malformed_sidecars_are_rejected_before_sorting(self):
        for spans in ({'A': []}, {'A': None}, {'A': ['2', 4]}):
            with self.assertRaises(ValueError):
                source_regions('f', spans, 10)

    def test_call_site_counts_come_from_records_not_label_prose(self):
        census = {'historical_size': 10, 'current_size': 2,
                  'regions': [{'start_offset': 0, 'end_offset': 10, 'label': 'unknown'}],
                  'historical_callees': [{'offset': 2, 'kind': 'call', 'name': 'f'},
                                         {'offset': 6, 'kind': 'indirect', 'name': None}],
                  'data_references': [], 'stack_frame': {'distinct_ebp_slots_referenced': 1,
                      'slots': [{'dwarf_candidates': [{'name': 'x'}, {'name': 'y'}]}]}}
        result = machine_regions(census)
        self.assertEqual(result['call_kinds_from_json'], {'call': 1, 'indirect': 1})
        self.assertEqual(result['multi_named_slot_count'], 1)
        self.assertFalse(result['slot_read_write_counts_are_liveness'])


if __name__ == '__main__':
    unittest.main()
