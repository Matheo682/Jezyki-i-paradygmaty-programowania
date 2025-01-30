module Task2

open System

// Definicja kursów wymiany
let exchangeRates = 
    Map.ofList [
        ("USD", 1.0)
        ("EUR", 0.85)
        ("GBP", 0.75)
        ("PLN", 3.8)
    ]

// Funkcja do przeliczania kwoty
let convertCurrency amount sourceCurrency targetCurrency =
    let sourceRate = exchangeRates.[sourceCurrency]
    let targetRate = exchangeRates.[targetCurrency]
    amount * (targetRate / sourceRate)

// Nowy moduł BMI
module BMI =
    // Funkcja do obliczania BMI
    let calculateBMI weight height =
        weight / ((height / 100.0) ** 2.0)

    // Funkcja do określenia kategorii BMI
    let getBMICategory bmi =
        if bmi < 18.5 then "Niedowaga"
        elif bmi < 24.9 then "Waga prawidłowa"
        elif bmi < 29.9 then "Nadwaga"
        else "Otyłość"