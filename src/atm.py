class ATM:
    """
    Klasa reprezentujÄca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """
    def __init__(self,money,pin):
        self.money = money
        self.pin = pin

    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :return: Saldo konta uĹźytkownika.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin != self.pin:
            raise ValueError("Nieprawidłowy pin")
        return self.money

        pass

    def deposit(self, pin: int, amount: float) -> float:
        """
        WpĹaca Ĺrodki na konto uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wpĹacenia.
        :return: Aktualne saldo po wpĹacie.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin != self.pin:
            raise ValueError("Nieprawidłowy pin")
        self.money += amount
        return self.money
        pass

    def withdraw(self, pin: int, amount: float) -> float:
        """
        WypĹaca Ĺrodki z konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wypĹacenia.
        :return: Aktualne saldo po wypĹacie.
        :raises InsufficientFundsException: JeĹli saldo jest niewystarczajÄce.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if pin != self.pin:
            raise ValueError("Nieprawidłowy pin")
        if amount > self.money:
            raise ValueError("Brak środków na koncie")
        self.money -= amount
        return self.money
        pass