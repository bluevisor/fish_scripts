function fish_greeting
    neofetch
    set -l line_count (wc -l < ~/greetings.txt)
    set -l random_line (random 1 $line_count)
    set -l quote (sed -n "$random_line"p ~/greetings.txt)
    echo $quote
    echo
end
