module Task3

open System
open System.Text.RegularExpressions

// Funkcja do liczenia liczby słów
let countWords (text: string) =
    let words = text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    words.Length

// Funkcja do liczenia liczby znaków (bez spacji)
let countCharacters (text: string) =
    text.Replace(" ", "").Length

// Funkcja do znajdowania najczęściej występującego słowa
let findMostFrequentWord (text: string) =
    let words = text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    let wordCounts = 
        words 
        |> Array.fold (fun acc word -> 
            if Map.containsKey word acc then 
                Map.add word (acc.[word] + 1) acc 
            else 
                Map.add word 1 acc) Map.empty
    wordCounts |> Map.toSeq |> Seq.maxBy snd |> fst