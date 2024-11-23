from datetime import datetime, timedelta

class VA3CDS:
    """Implementation of VAVS.3CDS:24 Compact Date Formatting"""

    CLASS_VERS = '24.A'
    CENTURY_START = datetime(2001, 1, 1)  # Base date for calculations
    BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    @staticmethod
    def base58_encode(num: int) -> str:
        """
        Encodes a number into Base58.
        
        Args:
            num (int): The number to encode.

        Returns:
            str: Base58-encoded string.
        """
        encoded = ""
        while num > 0:
            num, remainder = divmod(num, 58)
            encoded = VAVS_3CDS.BASE58_ALPHABET[remainder] + encoded
        return encoded or "1"

    @staticmethod
    def base58_decode(encoded: str) -> int:
        """
        Decodes a Base58-encoded string into a number.
        
        Args:
            encoded (str): The Base58-encoded string.

        Returns:
            int: Decoded number.
        """
        num = 0
        for char in encoded:
            num = num * 58 + VAVS_3CDS.BASE58_ALPHABET.index(char)
        return num

    @staticmethod
    def encode(date: datetime) -> str:
        """
        Encodes a given date into 3CDS format.

        Args:
            date (datetime): The date to encode.

        Returns:
            str: Encoded 3CDS string.
        """
        # Calculate the number of days since CENTURY_START
        delta_days = (date - VAVS_3CDS.CENTURY_START).days + 1  # Day 1 starts at 2001-01-01
        # Encode to Base58
        base58_encoded = VAVS_3CDS.base58_encode(delta_days)
        # Ensure 3-character fixed length
        base58_zfilled = base58_encoded.zfill(3)
        # Add prefix '('
        return f"({base58_zfilled}"

    @staticmethod
    def decode(encoded_date: str) -> datetime:
        """
        Decodes a 3CDS string back into a datetime object.

        Args:
            encoded_date (str): The 3CDS string to decode.

        Returns:
            datetime: Decoded date.
        """
        # Remove prefix '('
        base58_text = encoded_date.strip("(").lstrip("0")
        # Decode from Base58
        delta_days = VAVS_3CDS.base58_decode(base58_text)
        # Calculate the date
        return VAVS_3CDS.CENTURY_START + timedelta(days=delta_days - 1)


# Example Usage
if __name__ == "__main__":
    # Example date
    example_date = datetime(2024, 11, 23)
    # Encode the date
    encoded = VAVS_3CDS.encode(example_date)
    # Decode the encoded date
    decoded = VAVS_3CDS.decode(encoded)

    # Output results
    print(f"Original Date: {example_date}")
    print(f"Encoded 3CDS: {encoded}")
    print(f"Decoded Date: {decoded}")
