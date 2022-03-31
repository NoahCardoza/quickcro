
import csv
import os
import sys
from argparse import ArgumentParser
from datetime import datetime, timezone


def convert_crypto_csv(input_csv, output_csv=None):
    with open(input_csv, 'r') as fin, sys.stdout if output_csv is None else open(output_csv, 'w') as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, [
            'Date', 'Description', 'Original Description', 'Amount', 'Transaction Type', 'Category', 'Account Name', 'Lables', 'Notes'
        ])
        
        writer.writeheader()
        
        for row in reader:
            # convert timestamp from utc to local time
            timestamp = datetime.strptime(row['Timestamp (UTC)'], '%Y-%m-%d %H:%M:%S')
            timestamp = timestamp.replace(tzinfo=timezone.utc)
            timestamp = timestamp.astimezone()

            # write row to output
            tx_desc = row['Transaction Description']
            tx_amount = row['Amount']
            writer.writerow({
                'Date': timestamp.strftime('%m/%d/%Y'),
                'Description': tx_desc,
                'Original Description': tx_desc,
                'Amount': tx_amount,
                'Transaction Type': float(tx_amount) > 0 and 'credit' or 'debit',
                'Category': tx_desc.endswith(' -> USD') and 'Transfer' or 'Uncategorized',
                'Account Name': 'Crypto.com Royal Indigo',
                'Lables': '',
                'Notes': ''
            }) 


def main():
    parser = ArgumentParser(description='Convert a Crypto.com Debit Card transaction CSV export to one that\'s Quicken ready!', epilog='Fortune Favours the Brave!')

    parser.add_argument('input', help='Input CSV file')
    parser.add_argument('-o', '--output', dest='output', required=False, help='Output CSV file')

    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print('Input file does not exist: {}'.format(args.input))
        sys.exit(1)
    
    if args.output and os.path.exists(args.output):
        print('Output file already exists: {}'.format(args.output))
        try:
            input('Press Enter to overwrite, or Ctrl+C to cancel: ')
        except KeyboardInterrupt:
            print('\nAbort!')
            sys.exit(1)
    
    convert_crypto_csv(args.input, args.output)

    print('Success!')


if __name__ == '__main__':
    main()
