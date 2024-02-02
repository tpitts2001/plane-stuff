from sec_api import ExtractorApi

extractorApi = ExtractorApi("ed40254e3ea87bde6a3d276f88abe0fb7163ace50bb53516dcbd2a566ff3fa6c")

# 10-Q example
url_10q = "https://www.sec.gov/Archives/edgar/data/1318605/000095017022006034/aal-0000006201.htm"

part2_item_1A_text = extractorApi.get_section(url_10q, "part2item1a", "text")

print(url_10q)
