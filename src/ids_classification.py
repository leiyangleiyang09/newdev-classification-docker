import datetime
from ids_extraction import classify_e, classify_p, classify_d
from pytz import timezone


def offline_ids_classification(processing_list_dic: dict) -> str:
    result_csv = []
    i = 1
    total = len(processing_list_dic)
    execution_date = datetime.datetime.now(timezone('Australia/Sydney')).strftime("%Y-%m-%d %H:%M:%S")

    print(total)

    for sale_id in processing_list_dic:
        print('----------> Step 1. Process: %s (%s/%s)' % (sale_id, i, total))
        i = i + 1

        sale_id, property_id, prefix, summary, description, update_date, insert_date = processing_list_dic[sale_id]
        label, evidence = classify_p(prefix, summary, description)
        if label is None:
            label, evidence = classify_e(prefix, summary, description)
            if label is None:
                label, evidence = classify_d(prefix, summary, description)

        if label is None:
            label = 'N'
            evidence = 'NULL'
        evidence = evidence.replace('"', "'")
        insert_data = '","'.join([sale_id, property_id, insert_date, update_date, label, evidence, execution_date])
        print(insert_data)
        result_csv.append('"%s"' % insert_data)

    return '\n'.join(result_csv)
