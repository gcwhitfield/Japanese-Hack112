# George Whitfield 
# Hack 112 2018
# November 9 2018

class KeyMappings:
    
    hiraganaToKatakanaDict = {
        # -------- regular characters --------- # 
        'あ': 'ア',
        'い': 'イ',
        'う': 'ウ',
        'え': 'エ',
        'お': 'オ',

        'か': 'カ',
        'き': 'キ',
        'く': 'ク',
        'け': 'ケ',
        'こ': 'コ',
        
        'さ': 'サ',
        'し': 'シ',
        'す': 'ス',
        'せ': 'セ',
        'そ': 'ソ',

        'た': 'タ',
        'ち': 'チ',
        'つ': 'ツ',
        'て': 'テ',
        'と': 'ト',

        'な': 'ナ',
        'に': 'ニ',
        'ぬ': 'ヌ',
        'ね': 'ネ',
        'の': 'ノ',

        'は': 'ハ',
        'ひ': 'ヒ',
        'ふ': 'フ',
        'へ': 'ヘ',
        'ほ': 'ホ',

        'ま': 'マ',
        'み': 'ミ',
        'む': 'ム',
        'め': 'メ',
        'も': 'モ',

        'や': 'ヤ',
        'ゆ': 'ユ',
        'よ': 'ヨ',
        
        'ら': 'ラ',
        'り': 'リ',
        'る': 'ル',
        'れ': 'レ',
        'ろ': 'ロ',

        'わ': 'ワ',
        'ゐ': 'ヰ',
        'ゑ': 'ヱ',
        'を': 'ヲ',

        'ん': 'ン',

        # -------- combo hiragana --------- # 
 
        'にゃ': 'ニャ',
        'にゅ': 'ニュ',
        'にょ': 'ニョ',

        'ちゃ': 'チャ',
        'ちゅ': 'チュ',
        'ちょ': 'チョ',

        'しゃ': 'シャ',
        'しゅ': 'シュ',
        'しょ': 'ショ',

        'きゃ': 'キャ',
        'きゅ': 'キュ',
        'きょ': 'キョ',

        'りゃ': 'リャ',
        'りゅ': 'リュ',
        'りょ': 'リョ',

        'みゃ': 'ミャ',
        'みゅ': 'ミュ',
        'みょ': 'ミョ',

        'ひゃ': 'ヒャ',
        'ひゅ': 'ヒュ',
        'ひょ': 'ヒョ',

        'ぴゃ': 'ピャ',
        'ぴゅ': 'ピュ',
        'ぴょ': 'ピョ',
        
        'びゃ': 'ビャ',
        'びゅ': 'ビュ',
        'びょ': 'ビョ',

        'ぢゃ': 'ヂャ',
        'ぢゅ': 'ヂュ',
        'ぢょ': 'ヂョ',

        'じゃ': 'ジャ',
        'じゅ': 'ジュ',
        'じょ': 'ジョ',
        
        # -------- dakuten --------- # 

        'ぱ': 'パ',
        'ぴ': 'ピ',
        'ぷ': 'プ',
        'ぺ': 'ペ',
        'ぽ': 'ポ',
        
        'ば': 'バ',
        'び': 'ビ',
        'ぶ': 'ブ',
        'べ': 'ベ',
        'ぼ': 'ボ',

        'だ': 'ダ',
        'ぢ': 'ヂ',
        'づ': 'ヅ',
        'で': 'デ',
        'ど': 'ド',

        'ざ': 'ザ',
        'じ': 'ジ',
        'ず': 'ズ',
        'ぜ': 'ゼ',
        'ぞ': 'ゾ',

        'が': 'ガ',
        'ぎ': 'ギ',
        'ぐ': 'グ',
        'げ': 'ゲ',
        'ご': 'ゴ'
   }

    romajiDictionary = {
        # -------- regular characters --------- # 
        'a': 'あ',
        'i': 'い',
        'u': 'う',
        'e': 'え',
        'o': 'お',

        'ka': 'か',
        'ki': 'き',
        'ku': 'く',
        'ke': 'け',
        'ko': 'こ',

        'sa': 'さ',
        'si': 'し',
        'shi': 'し',
        'su': 'す',
        'se': 'せ',
        'so': 'そ',

        'ta': 'た',
        'ti': 'ち',
        'chi': 'ち',
        'tsu': 'つ',
        'tu': 'つ',
        'te': 'て',
        'to': 'と',

        'na': 'な',
        'ni': 'に',
        'nu': 'ぬ',
        'ne': 'ね',
        'no': 'の',

        'ha': 'は',
        'hi': 'ひ',
        'hu': 'ふ',
        'fu': 'ふ',
        'he': 'へ',
        'ho': 'ほ',

        'ma': 'ま',
        'mi': 'み',
        'mu': 'む',
        'me': 'め',
        'mo': 'も',

        'ya': 'や',
        'yu': 'ゆ',
        'yo': 'よ',

        'ra': 'ら',
        'ri': 'り',
        'ru': 'る',
        're': 'れ',
        'ro': 'ろ',

        'wa': 'わ',
        'wi': 'ゐ', # special
        'we': 'ゑ', # special
        'wo': 'を',

        'nn': 'ん',

        # -------- combo hiragana --------- # 
 
        'nya': 'にゃ',
        'nyu': 'にゅ',
        'nyo': 'にょ',

        'cha': 'ちゃ',
        'chu': 'ちゅ',
        'cho': 'ちょ',

        'sha': 'しゃ',
        'shu': 'しゅ',
        'sho': 'しょ',

        'kya': 'きゃ',
        'kyu': 'きゅ',
        'kyo': 'きょ',

        'rya': 'りゃ',
        'ryu': 'りゅ',
        'ryo': 'りょ',

        'mya': 'みゃ',
        'myu': 'みゅ',
        'myo': 'みょ',

        'hya': 'ひゃ',
        'hyu': 'ひゅ',
        'hyo': 'ひょ',

        'pya': 'ぴゃ',
        'pyu': 'ぴゅ',
        'pyo': 'ぴょ',
        
        'bya': 'びゃ',
        'byu': 'びゅ',
        'byo': 'びょ',

        'dya': 'ぢゃ',
        'dyu': 'ぢゅ',
        'dyo': 'ぢょ',

        'jya': 'じゃ',
        'jyu': 'じゅ',
        'jyo': 'じょ',
        
        # -------- dakuten --------- # 

        'pa': 'ぱ',
        'pi': 'ぴ',
        'pu': 'ぷ',
        'pe': 'ぺ',
        'po': 'ぽ',
        
        'ba': 'ば',
        'bi': 'び',
        'bu': 'ぶ',
        'be': 'べ',
        'bo': 'ぼ',

        'da': 'だ',
        'di': 'ぢ',
        'du': 'づ',
        'de': 'で',
        'do': 'ど',

        'za': 'ざ',
        'ji': 'じ',
        'zi': 'じ',
        'zu': 'ず',
        'ze': 'ぜ',
        'zo': 'ぞ',

        'ga': 'が',
        'gi': 'ぎ',
        'gu': 'ぐ',
        'ge': 'げ',
        'go': 'ご',

    }

    @staticmethod
    def romajiToHiragana(romaji): # give the hiragana of the romaji
        if romaji in KeyMappings.romajiDictionary:
            return KeyMappings.romajiDictionary[romaji]
        else:
            return None

    @staticmethod
    def hiraganaToKatakana(hirag): # convert hiragana to katana
        if hirag in KeyMappings.hiraganaToKatakanaDict:
            return KeyMappings.hiraganaToKatakanaDict[hirag]
        else:
            return None

    @staticmethod
    def katakanaToHiragana(kata):
        for element in KeyMappings.hiraganaToKatakanaDict:
            if KeyMappings.hiraganaToKatakanaDict[element] == kata:
                return element
        return None
        