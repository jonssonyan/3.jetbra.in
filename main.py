import json

from lxml import etree


def get_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_html(file_path):
    return etree.parse(file_path, etree.HTMLParser())


if __name__ == '__main__':
    keys_json = get_json('keys_origin.json')
    index_html = get_html('index.html')
    articles = index_html.xpath('/html/body/main/article')
    key_direct = {}
    for item in articles:
        data_sequence = item.xpath('@data-sequence')
        data_sequence_name = item.xpath('div/h1/text()')
        if len(data_sequence) > 0 and len(data_sequence_name) > 0:
            key_direct[data_sequence_name[0]] = keys_json[data_sequence[0]]

    if len(key_direct) > 0:
        f = open('keys.json', 'w')
        a = json.dumps(key_direct)
        f.write(a)
        f.close()
