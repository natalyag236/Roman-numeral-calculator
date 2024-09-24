use std::collections::HashMap;
use std::io::{self,Write};

fn main() {
    let mut input = String::new();
    print!("Enter a string: ");
    io::stdout().flush().unwrap(); 

   
    io::stdin()
        .read_line(&mut input)
        .expect("Failed: to read user input ");
       

    let mut counter = 0;
    let mut char_count: HashMap<char, i32> = HashMap::new(); 

    for ch in input.chars() {
        counter += 1;

        let count = char_count.entry(ch).or_insert(0);
        *count += 1;
    }

    let mut max_char = ' ';
    let mut max_count = 0;

    for (ch, count) in &char_count {
        if *count > max_count {
            max_count = *count;
            max_char = *ch;
        }
    }

    println!("Total num of characters: {}", counter); 

    if max_count > 1 {
        println!("The most frequent occurring character is '{}' and appears {} times.", max_char, max_count);
    }
}
