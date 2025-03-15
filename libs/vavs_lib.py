from datetime import date, timedelta

class VA3CDD:
    """Implementation of VAVS.3CDS:24 Compact Date Formatting"""

    def __init__(self):
        self.c_class_vers = '25.A'
        #+ Base date for calculations
        self.c_century_start = date(1970, 1, 1)
        self.c_base58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    def base58_encode(self, a_int2enc: int) -> str:
        """
        Encodes a number into Base58.
        
        Args:
            a_int2enc (int): The number to encode.

        Returns:
            str: Base58-encoded string.
        """
        x_encoded_string = ""
        while a_int2enc > 0:
            a_int2enc, x_remainder = divmod(a_int2enc, 58)
            x_encoded_string = self.c_base58_alphabet[x_remainder] + x_encoded_string
        return x_encoded_string or "1"

    def base58_decode(self, a_str2dec: str) -> int:
        """
        Decodes a Base58-encoded string into a number.
        
        Args:
            a_str2dec (str): The Base58-encoded string.

        Returns:
            int: Decoded number.
        """
        x_decoded_num = 0
        for x_char in a_str2dec:
            x_decoded_num = x_decoded_num * 58 + self.c_base58_alphabet.index(x_char)
        return x_decoded_num

    def date_encode(self, a_date2enc: date) -> str:
        """
        Encodes a given date into 3CDS format.

        Args:
            a_date2enc (datetime): The date to encode.

        Returns:
            str: Encoded 3CDS string.
        """
        #+ Calculate the number of days since CENTURY_START
        x_delta_days = (a_date2enc - self.c_century_start).days + 1
        #+ Encode to Base58
        x_base58_encoded = self.base58_encode(x_delta_days)
        # Ensure 3-character fixed length
        x_base58_zfill = x_base58_encoded.zfill(3)
        # Add prefix '('
        return "["+f"{x_base58_zfill}"

    def date_decode(self, a_str2dec: str) -> date:
        """
        Decodes a 3CDS string back into a datetime object.

        Args:
            a_str2dec (str): The 3CDS string to decode.

        Returns:
            datetime: Decoded date.
        """
        # Remove prefix '('
        x_base58_text = a_str2dec.strip("[").lstrip("0")
        # Decode from Base58
        x_delta_days = self.base58_decode(x_base58_text)
        # Calculate the date
        return self.c_century_start + timedelta(days=x_delta_days - 1)


# Example Usage
if __name__ == "__main__":
    # Initialize the encoder/decoder
    x_worker = VA3CDD()
    # Example date
    x_work_date = date(2024, 11, 23)
    # Encode the date
    x_encoded = x_worker.date_encode(x_work_date)
    # Decode the encoded date
    x_decoded = x_worker.date_decode(x_encoded)

    # Output results
    print(f"Original Date: {x_work_date}")
    print(f"Encoded 3CDS: {x_encoded}")
    print(f"Decoded Date: {x_decoded}")
