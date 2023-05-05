from model.griffon_pdf import GriffonPdf


class GriffonPdfWithAlternativeExtract(GriffonPdf):
    # Добавлен в качестве примера другого возможного подхода
    def extract_data(self):
        labels = {'SN:', 'DESCRIPTION:', 'MFG', 'DOM', 'LOT'}
        values = {}
        lines = self.pdf_text.split('\n')
        for line in lines:
            if 'GRIFFON AVIATION SERVICES LLC' in line:
                values['COMPANY'] = line.strip()
            elif 'PN:' in line:
                pn_start = line.find('PN:') + len('PN:')
                pn_end = line.find('SN:') - 1
                values['PN'] = line[pn_start:pn_end].strip()
            else:
                for label in labels:
                    if label in line:
                        values[label] = line.split(':')[-1].strip()
                        break
            if 'DESCRIPTION:' in line:
                values['DESCRIPTION'] = line.split(':')[-1].strip()
            elif 'LOCATION:' in line:
                values['LOCATION'] = line.split(' ')[1]
                values['CONDITION'] = line.split(' ')[3]
            elif 'RECEIVER#:' in line:
                values['RECEIVER#'] = line.split(' ')[1]
                values['UOM'] = line.split(' ')[3]
            elif 'EXP DATE:' in line:
                pn_start = line.find('EXP DATE:') + len('EXP DATE:')
                pn_end = line.find('PO:') - 1
                values['EXP DATE'] = line[pn_start:pn_end].strip()
                values['PO'] = line.split(' ')[4]
            elif 'CERT SOURCE:' in line:
                values['CERT SOURCE'] = line.split(':')[-1].strip()
            elif 'REC.DATE:' in line:
                pn_start = line.find('REC.DATE:') + len('REC.DATE:')
                pn_end = line.find('MFG:') - 1
                values['REC.DATE'] = line[pn_start:pn_end].strip()
            elif 'MFG:' in line:
                values['MFG'] = line.split(':')[-1].strip()
            elif 'BATCH# :' in line:
                values['BATCH#'] = line.split(' ')[2]
                values['DOM'] = line.split(' ')[4]
            elif 'DOM:' in line:
                values['DOM'] = line.split(':')[-1].strip()
            elif 'REMARK:' in line:
                pn_start = line.find('REMARK:') + len('REMARK:')
                pn_end = line.find('LOT# :') - 1
                values['REMARK'] = line[pn_start:pn_end].strip()
            elif 'LOT# :' in line:
                values['LOT'] = line.split(':')[-1].strip()
            elif 'TAGGED BY:' in line:
                values['TAGGED BY:'] = line.split(' ')[2]
            elif 'NOTES:' in line:
                if 'Qty:' in line:
                    values['NOTES'] = ''
                else:
                    values['NOTES'] = line[line.find('NOTES:'):]
            elif 'Qty:' in line:
                pn_start = line.find('Qty:') + len('Qty:')
                pn_end = line.find('NOTES:')
                values['Qty'] = line[pn_start:pn_end].strip()
        return values
