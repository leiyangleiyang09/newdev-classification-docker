from util.ids_pattern import p_patterns_pos, e_patterns_pos, d_priceprefix_group_1_pos, \
    d_priceprefix_group_1_neg, d_priceprefix_group_2_pos, d_priceprefix_group_2_neg, d_priceprefix_group_3_pos, \
    d_priceprefix_group_3_neg, d_priceprefix_group_4_pos, d_priceprefix_group_4_neg, d_priceprefix_group_5_pos, \
    d_priceprefix_group_6_pos, d_summary_group_1_pos, d_summary_group_1_neg, d_summary_group_2_pos, \
    d_summary_group_2_neg, d_summary_group_3_pos, d_summary_group_3_neg, d_summary_group_4_pos, d_summary_group_4_neg, \
    d_summary_group_5_pos, d_summary_group_5_neg, d_summary_group_6_pos, d_summary_group_7_pos, \
    d_description_group_1_pos


def classify_p(prefix: str, summary: str, description: str) -> tuple:
    label = None
    evidence = None

    for p_pattern in p_patterns_pos:
        if p_pattern in prefix:
            label = 'P'
            evidence = prefix
            break
        elif p_pattern in summary:
            label = 'P'
            evidence = summary
            break
        elif p_pattern in description:
            label = 'P'
            pattern_index = description.find(p_pattern)
            if pattern_index != -1:
                if pattern_index - 20 < 0:
                    pattern_start = 0
                else:
                    pattern_start = pattern_index - 20
                if pattern_index + len(p_pattern) + 20 > len(description):
                    pattern_end = len(description)
                else:
                    pattern_end = pattern_index + len(p_pattern) + 20
                evidence = description[pattern_start:pattern_end]
            break
    return label, evidence


def classify_e(prefix: str, summary: str, description: str) -> tuple:
    label = None
    evidence = None

    for e_pattern in e_patterns_pos:
        if e_pattern in prefix:
            label = 'E'
            evidence = prefix
            break
        elif e_pattern in summary:
            label = 'E'
            evidence = summary
            break
        elif e_pattern in description:
            label = 'E'
            pattern_index = description.find(e_pattern)
            if pattern_index != -1:
                if pattern_index - 20 < 0:
                    pattern_start = 0
                else:
                    pattern_start = pattern_index - 20
                if pattern_index + len(e_pattern) + 20 > len(description):
                    pattern_end = len(description)
                else:
                    pattern_end = pattern_index + len(e_pattern) + 20
                evidence = description[pattern_start:pattern_end]
            break
    return label, evidence


def classify_d(prefix: str, summary: str, description: str) -> tuple:
    label = None
    evidence = None

    for d_pattern_1 in d_priceprefix_group_5_pos:
        if d_pattern_1 in prefix:
            label = 'D'
            evidence = prefix
            break
    if label is None:
        for (d_pattern_1, d_pattern_2) in d_priceprefix_group_6_pos:
            if d_pattern_1 in prefix and d_pattern_2 in prefix:
                label = 'D'
                evidence = prefix
                break

    if label is None:
        for (d_priceprefix_group_pos, d_priceprefix_group_neg) \
                in [(d_priceprefix_group_1_pos, d_priceprefix_group_1_neg),
                    (d_priceprefix_group_2_pos, d_priceprefix_group_2_neg),
                    (d_priceprefix_group_3_pos, d_priceprefix_group_3_neg)]:
            neg_label = False
            for d_pattern_1 in d_priceprefix_group_neg:
                if d_pattern_1 in prefix:
                    neg_label = True
                    break
            if neg_label is False:
                for (d_pattern_1, d_pattern_2) in d_priceprefix_group_pos:
                    if d_pattern_1 in prefix and d_pattern_2 in prefix:
                        label = 'D'
                        evidence = prefix
                        break
    if label is None:
        neg_label = False
        for d_pattern_1 in d_priceprefix_group_4_neg:
            if d_pattern_1 in prefix:
                neg_label = True
                break
        if neg_label is False:
            for d_pattern_1 in d_priceprefix_group_4_pos:
                if d_pattern_1 in prefix:
                    label = 'D'
                    evidence = prefix
                    break

    if label is None:
        for d_pattern_1 in d_summary_group_6_pos:
            if d_pattern_1 in summary:
                label = 'D'
                evidence = summary
                break
    if label is None:
        for (d_pattern_1, d_pattern_2) in d_summary_group_7_pos:
            if d_pattern_1 in summary and d_pattern_2 in summary:
                label = 'D'
                evidence = summary
                break
    if label is None:
        for (d_summary_group_pos, d_summary_group_neg) \
                in [(d_summary_group_1_pos, d_summary_group_1_neg),
                    (d_summary_group_2_pos, d_summary_group_2_neg),
                    (d_summary_group_4_pos, d_summary_group_4_neg)]:
            neg_label = False
            for d_pattern_1 in d_summary_group_neg:
                if d_pattern_1 in summary:
                    neg_label = True
                    break
            if neg_label is False:
                for (d_pattern_1, d_pattern_2) in d_summary_group_pos:
                    if d_pattern_1 in summary and d_pattern_2 in summary:
                        label = 'D'
                        evidence = summary
                        break
    if label is None:
        for (d_summary_group_pos, d_summary_group_neg) \
                in [(d_summary_group_3_pos, d_summary_group_3_neg),
                    (d_summary_group_5_pos, d_summary_group_5_neg)]:
            neg_label = False
            for d_pattern_1 in d_summary_group_neg:
                if d_pattern_1 in summary:
                    neg_label = True
                    break
            if neg_label is False:
                for d_pattern_1 in d_summary_group_pos:
                    if d_pattern_1 in summary:
                        label = 'D'
                        evidence = summary
                        break

    if label is None:
        for d_pattern in d_description_group_1_pos:
            if d_pattern in description:
                label = 'D'
                pattern_index = description.find(d_pattern)
                if pattern_index != -1:
                    if pattern_index - 20 < 0:
                        pattern_start = 0
                    else:
                        pattern_start = pattern_index - 20
                    if pattern_index + len(d_pattern) + 20 > len(description):
                        pattern_end = len(description)
                    else:
                        pattern_end = pattern_index + len(d_pattern) + 20
                    evidence = description[pattern_start:pattern_end]
                break
    return label, evidence
