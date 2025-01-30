module Task4

open System

// Definicja rekordu dla konta bankowego
type Account = {
    AccountNumber: string
    Balance: float
}

// Mapa do przechowywania kont bankowych
let mutable accounts = Map.empty<string, Account>

// Funkcja do tworzenia nowego konta
let createAccount accountNumber =
    if Map.containsKey accountNumber accounts then
        printfn "Konto o numerze %s już istnieje." accountNumber
    else
        let newAccount = { AccountNumber = accountNumber; Balance = 0.0 }
        accounts <- Map.add accountNumber newAccount accounts
        printfn "Utworzono nowe konto o numerze %s." accountNumber

// Funkcja do depozytowania środków na konto
let deposit accountNumber amount =
    if Map.containsKey accountNumber accounts then
        let account = accounts.[accountNumber]
        let updatedAccount = { account with Balance = account.Balance + amount }
        accounts <- Map.add accountNumber updatedAccount accounts
        printfn "Wpłacono %.2f na konto %s. Nowe saldo: %.2f" amount accountNumber updatedAccount.Balance
    else
        printfn "Konto o numerze %s nie istnieje." accountNumber

// Funkcja do wypłacania środków z konta
let withdraw accountNumber amount =
    if Map.containsKey accountNumber accounts then
        let account = accounts.[accountNumber]
        if account.Balance >= amount then
            let updatedAccount = { account with Balance = account.Balance - amount }
            accounts <- Map.add accountNumber updatedAccount accounts
            printfn "Wypłacono %.2f z konta %s. Nowe saldo: %.2f" amount accountNumber updatedAccount.Balance
        else
            printfn "Niewystarczające środki na koncie %s." accountNumber
    else
        printfn "Konto o numerze %s nie istnieje." accountNumber

// Funkcja do wyświetlania salda konta
let displayBalance accountNumber =
    if Map.containsKey accountNumber accounts then
        let account = accounts.[accountNumber]
        printfn "Saldo konta %s wynosi: %.2f" accountNumber account.Balance
    else
        printfn "Konto o numerze %s nie istnieje." accountNumber