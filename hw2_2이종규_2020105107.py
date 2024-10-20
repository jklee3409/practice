def vowel_number_calculation(term_list):
    vowel_list = {'a', 'e', 'i', 'o', 'u'}

    sum_vowel_count = 0
    max_count = 0
    max_term = ""

    for term in list:
        count = 0
        for char in term:
            if char in vowel_list:
                count += 1
                sum_vowel_count += 1
        if count > max_count:
            max_count = count
            max_term = term

    return sum_vowel_count, max_term, max_count

list = ['it','is','rather','for','us','to','be','here','dedicated','to',
        'the','great','task','remaining','before','us','that','from','these','honored',
        'dead','we','take','increased','devotion','to','that','cause','for','which',
        'they','gave','the','last','full','measure','of','devotion','that','we',
        'here','highly','resolve','that','these','dead','shall','not','have','died',
        'in','vain','that','this','nation','under','god','shall','have','a',
        'new','birth','of','freedom','and','that','government','of','the','people',
        'by','the','people', 'for','the','people','shall','not','perish','from',
        'the','earth']

print(vowel_number_calculation(list))
