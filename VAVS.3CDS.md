# VAVS.3CDS:24.A - Compact Data Formatting

VAVS.3CDT is an attempt to shorten date representation in a reversible way, to the least reasonable length while using in date stamping needs where the length of the string is important (e.x. file names).
While the standard doesn't consider human readability in regular conditions, it remains textually sortable and thus is a proper fit for its main aim, stamping files.

Calculation:
1. Calculation is taken of the number of days starting from the begining of the century (Where '2001-01-01' is the Day 1).
2. The resulting number is encoded with Base58 encoding.
3. Resulting bytes are encoded to text
4. To ensure fixed 3 char length, the text is zfilled for 3 chars (zfilling = filling with leading zeroes using Python zfill). Using 0 is not a problem as it is not presented in Base58.
5. Prefix "(" is added to the resulting 3 char combination.
6. The date stamp of the initial version of this standard is '2024-11-23' or in 3CDT format - '(3bV'.

Decoding is done via reversing the algorithm, while extra '0'-s are stripped initially.

Note: 3CDS is also used as a base for the sibling timstamping formats
