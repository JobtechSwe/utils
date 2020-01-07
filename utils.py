import re
import collections


class Advertisements:
    def __init__(self, ads):
        self.ads = ads

    def build_dictionary_lastname(self):
        # build Trie Dictionary for last name
        dictionary_lastname = collections.defaultdict()
        with open('last_name.txt', 'r') as file:
            for line in file.readlines():
                dic = dictionary_lastname
                for w in line.rstrip("\n"):
                    dic = dic.setdefault(w, {})
                dic.setdefault('_end')
        return dictionary_lastname

    def build_dictionary_firstname(self):
        # build Trie Dictionary for first name
        dictionary_firstname = collections.defaultdict()
        with open('first_name.txt', 'r') as file:
            for line in file.readlines():
                dic = dictionary_firstname
                for w in line.rstrip("\n"):
                    dic = dic.setdefault(w, {})
                dic.setdefault('_end')
        return dictionary_firstname

    def check_name(self, word: str, dictionary):
        name = dictionary
        for letter in word:
            if letter not in name:
                return False
            name = name[letter]
        if "_end" in name:
            return True
        return False

    def find_name(self, ads: str):
        ads = ads.split(' ')
        length = len(ads)
        dictionary_firstname = self.build_dictionary_firstname()
        dictionary_lastname = self.build_dictionary_lastname()
        i = 0
        while i < length:
            if self.check_name(ads[i], dictionary_firstname):
                next = i + 1
                while next < length:
                    if self.check_name(ads[next], dictionary_lastname):
                        next += 1
                    else:
                        break
                if next - i > 1:
                    ads[i:next] = '**NAME***'
                    i = next - 1
            i += 1
        return ' '.join(ads)

    def mask_sensitive_info(self, ads: str) -> str:
        email_regex = '\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})'
        personal_no_regex = '\d{6,8}[-|(\s)]{0,1}[T|\d]\d{3}'
        telephone_regex = r'(?:\B\+ ?49|\b0)(?: *[(-]? *\d(?:[ \d]*\d)?)? *(?:[)-] *)?\d+ *(?:[/)-] *)?\d+ *(?:[/)-] *)?\d+(?: *- *\d+)?'
        result = re.sub(email_regex, '**EMAIL***', ads)
        result = re.sub(personal_no_regex, '**PERSONAL NO**', result)
        result = re.sub(telephone_regex, '**TELEPHONE NO**', result)
        result = self.find_name(result)
        return result
