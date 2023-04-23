import csv
import xml.etree.ElementTree as ET

# Create a list of all FinInstrmGnlAttrbts elements
with open('output1.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp', 'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'])

    # Parse the XML file and find all FinInstrmGnlAttrbts elements
    tree = ET.parse('SteelEye_assessment_xml_file.xml')
    root = tree.getroot()
    namespaces = {'a': 'urn:iso:std:iso:20022:tech:xsd:auth.036.001.02'}
    elems = root.findall('.//a:FinInstrmGnlAttrbts', namespaces)

    # Loop over the FinInstrmGnlAttrbts elements and write the values to the CSV file
    count = 0
    for elem in elems:
        id = elem.get('Id', '').strip()
        full_nm = elem.get('FullNm', '').strip()
        clssfctn_tp = elem.get('ClssfctnTp', '').strip()
        cmmdty_deriv_ind = elem.get('CmmdtyDerivInd', '').strip()
        ntnl_ccy = elem.get('NtnlCcy', '').strip()
        issr = elem.find('.//a:Issr', namespaces).text.strip() if elem.find('.//a:Issr', namespaces) is not None and elem.find('.//a:Issr', namespaces).text else ''

        # Write the values to the CSV file
        writer.writerow([id, full_nm, clssfctn_tp, cmmdty_deriv_ind, ntnl_ccy, issr])
        count += 1

    print("Wrote " + str(count) + " rows to output1.csv")
