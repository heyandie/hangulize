# -*- coding: utf-8 -*-
from hangulize import *


class ModernGreek(Language):
    """For transcribing Modern Greek."""

    vowels = u'αάεέηήιίϊοόυύϋωώΥ'
    cs = u'βγδζθκλμνξπρστφχψΙΝΤΧ'
    vl = u'θκξπστφχψΤΧ'
    v = u'βγδζλμνρΙΝ'
    s = u'λμνρ'
    notation = Notation([
        (u'(<sv>)\u0300', u'(<av>)'),
        (u'\u0300', None),
        (u'(<sv>)\u0301', u'(<av>)'),
        (u'\u0301', None),
        (u'(<sv>)\u0342', u'(<av>)'),
        (u'\u0342', None),
        (u'\u0344', u'\u0308'),
        (u'ι\u0308', u'ϊ'),
        (u'ί\u0308', u'ϊ'),
        (u'υ\u0308', u'ϋ'),
        (u'ύ\u0308', u'ϋ'),
        (u'\u0304', None),
        (u'\u0313', None),
        (u'\u0343', None),
        (u'\u0314', None),
        (u'\u1FDD', None),
        (u'\u1FDE', None),
        (u'\u1FDF', None),
        (u'\u1FFE', None),
        (u'{@}ϊ{@}', u'-ι-'),
        (u'{@}ϊ', u'-ι'),
        (u'ϊ{@}', u'ι-'),
        (u'ϊ', u'ι'),
        (u'{@}ϋ{@}', u'-υ-'),
        (u'{@}ϋ', u'-υ'),
        (u'ϋ{@}', u'υ-'),
        (u'ϋ', u'υ'),
        (u'{α|ε|η}υ{@|<v>}', u'β'),
        (u'{α|ε|η}ύ{@|<v>}', u'β'),
        (u'{α|ε|η}υ', u'φ'),
        (u'{α|ε|η}ύ', u'φ'),
        (u'αι', u'ε'),
        (u'ει', u'ι'),
        (u'οι', u'ι'),
        (u'ου', u'Υ'),
        (u'υι', u'ι'),
        (u'η', u'ι'),
        (u'υ', u'ι'),
        (u'{@}γγι', u'Νγ-ι'),
        (u'γι{@}', u'Ι'),
        (u'αί', u'ε'),
        (u'εί', u'ι'),
        (u'οί', u'ι'),
        (u'ού', u'Υ'),
        (u'υί', u'ι'),
        (u'ά', u'α'),
        (u'έ', u'ε'),
        (u'ή', u'ι'),
        (u'ί', u'ι'),
        (u'ό', u'ο'),
        (u'ύ', u'ι'),
        (u'ω', u'ο'),
        (u'ώ', u'ο'),
        (u'{@}γγ{ε|ι}', u'Νγ-'),
        (u'γ{ε|ι}', u'Ι'),
        (u'{@}νγ{κ|ξ}', u'γ'),
        (u'{@}νκτ', u'γκτ'),
        (u'{@}γγ', u'Νγ'),
        (u'{@}γκ{@|<s>}', u'Νγ'),
        (u'{@}γκ', u'Ν'),
        (u'{@}γ{ξ|χ}', u'Ν'),
        (u'γκ', u'γ'),
        (u'μπ{τ}', u'μ'),
        (u'{@}μπ', u'μβ'),
        (u'{@}μπ', u'μβ'),
        (u'μπ', u'β'),
        (u'{@}ν{γ|κ|χ}', u'Ν'),
        (u'{@}ντζ', u'νζ'),
        (u'{@}ντσ', u'νΤ'),
        (u'{@}ντ', u'νδ'),
        (u'ντ', u'δ'),
        (u'τζ', u'ζ'),
        (u'τσ', u'Τ'),
        (u'ξ', u'κσ'),
        (u'ψ', u'πσ'),
        (u'ββ', u'β'),
        (u'γγ', u'γ'),
        (u'δδ', u'δ'),
        (u'ζζ', u'ζ'),
        (u'θθ', u'θ'),
        (u'κκ', u'κ'),
        (u'^κχ', u'Χ'),
        (u'κχ{β|γ|δ|ζ|κ|μ|ξ|π|σ|φ|χ|ψ|Ι|Τ}', u'Χ'),
        (u'λλ', u'λ'),
        (u'μμ', u'μ'),
        (u'νν', u'ν'),
        (u'ππ', u'π'),
        (u'πφ', u'φ'),
        (u'ρρ', u'ρ'),
        (u'σσ', u'σ'),
        (u'ττ', u'τ'),
        (u'τθ', u'θ'),
        (u'φφ', u'φ'),
        (u'χχ', u'χ'),
        (u'^κ', u'κ;'),
        (u'{<cs>}κ', u'κ;'),
        (u'κ{<vl>}', u'κ,'),
        (u'^π', u'π;'),
        (u'{<cs>}π', u'π;'),
        (u'π{<vl>}', u'π,'),
        (u';', None),
        (u'Χ', u'κ'),
        (u'^λ', u'λ;'),
        (u'^μ', u'μ;'),
        (u'^ν', u'ν;'),
        (u'λ$', u'λ,'),
        (u'μ$', u'μ,'),
        (u'ν$', u'ν,'),
        (u'λ{@|μ,|ν,}', u'λ;'),
        (u'μ{@}', u'μ;'),
        (u'ν{@}', u'ν;'),
        (u'λ', u'λ,'),
        (u'μ', u'μ,'),
        (u'ν', u'ν,'),
        (u'Ν', u'Ν,'),
        (u',,', u','),
        (u',;', None),
        (u',λ,', u'λ,'),
        (u',μ,', u'μ,'),
        (u',ν,', u'ν,'),
        (u'λ{μ;|ν;}', u'λ,'),
        (u';', None),
        (u'{<cs>}Ι', u'ΨΙ'),
        (u'β', Choseong(B)),
        (u'γ', Choseong(G)),
        (u'δ', Choseong(D)),
        (u'ζ', Choseong(J)),
        (u'θ', Choseong(T)),
        (u'κ,', Jongseong(G)),
        (u'κ', Choseong(K)),
        (u'^λ', Choseong(L)),
        (u'{,}λ', Choseong(L)),
        (u'λ,', Jongseong(L)),
        (u'λ', Jongseong(L), Choseong(L)),
        (u'μ,', Jongseong(M)),
        (u'μ', Choseong(M)),
        (u'ν,', Jongseong(N)),
        (u'ν', Choseong(N)),
        (u'Ν', Jongseong(NG)),
        (u'π,', Jongseong(B)),
        (u'π', Choseong(P)),
        (u'ρ', Choseong(L)),
        (u'σ', Choseong(S)),
        (u'τ', Choseong(T)),
        (u'Τ', Choseong(C)),
        (u'φ', Choseong(P)),
        (u'χ', Choseong(H)),
        (u'Ια', Jungseong(YA)),
        (u'Ιε', Jungseong(YE)),
        (u'Ιι', Jungseong(I)),
        (u'Ιο', Jungseong(YO)),
        (u'ΙΥ', Jungseong(YU)),
        (u'α', Jungseong(A)),
        (u'ε', Jungseong(E)),
        (u'ι', Jungseong(I)),
        (u'ο', Jungseong(O)),
        (u'Υ', Jungseong(U)),
        (u'Ψ', Choseong(NG))
    ])

    def normalize(self, string):
        def normalize_only_unsafe(string):
            map = {u'Α': u'α',
                   u'Ἀ': u'α',
                   u'ᾼ': u'α',
                   u'ᾈ': u'α',
                   u'ἀ': u'α',
                   u'ᾳ': u'α',
                   u'ᾀ': u'α',
                   u'Ᾱ': u'α',
                   u'Ᾰ': u'α',
                   u'ᾱ': u'α',
                   u'ᾰ': u'α',
                   u'Ἁ': u'α',
                   u'ᾉ': u'α',
                   u'ᾁ': u'α',
                   u'Ά': u'ά',
                   u'Ὰ': u'ά',
                   u'Ἄ': u'ά',
                   u'Ἂ': u'ά',
                   u'Ἆ': u'ά',
                   u'ᾌ': u'ά',
                   u'ᾊ': u'ά',
                   u'ᾎ': u'ά',
                   u'ὰ': u'ά',
                   u'ᾶ': u'ά',
                   u'ἄ': u'ά',
                   u'ἂ': u'ά',
                   u'ἆ': u'ά',
                   u'ᾴ': u'ά',
                   u'ᾲ': u'ά',
                   u'ᾷ': u'ά',
                   u'ᾄ': u'ά',
                   u'ᾂ': u'ά',
                   u'ᾆ': u'ά',
                   u'Ἅ': u'ά',
                   u'Ἃ': u'ά',
                   u'Ἇ': u'ά',
                   u'ᾍ': u'ά',
                   u'ᾋ': u'ά',
                   u'ᾏ': u'ά',
                   u'ἃ': u'ά',
                   u'ἇ': u'ά',
                   u'ᾅ': u'ά',
                   u'ᾃ': u'ά',
                   u'ᾇ': u'ά',
                   u'Β': u'β',
                   u'Γ': u'γ',
                   u'Δ': u'δ',
                   u'Ε': u'ε',
                   u'Ἐ': u'ε',
                   u'ἐ': u'ε',
                   u'Ἑ': u'ε',
                   u'Έ': u'έ',
                   u'Ὲ': u'έ',
                   u'Ἔ': u'έ',
                   u'Ἒ': u'έ',
                   u'έ': u'έ',
                   u'ὲ': u'έ',
                   u'ἔ': u'έ',
                   u'ἒ': u'έ',
                   u'Ἕ': u'έ',
                   u'Ἓ': u'έ',
                   u'ἓ': u'έ',
                   u'Ζ': u'ζ',
                   u'Η': u'η',
                   u'Ἠ': u'η',
                   u'ῌ': u'η',
                   u'ᾘ': u'η',
                   u'ἠ': u'η',
                   u'ῃ': u'η',
                   u'ᾐ': u'η',
                   u'Ἡ': u'η',
                   u'ᾙ': u'η',
                   u'ᾑ': u'η',
                   u'Ή': u'ή',
                   u'Ὴ': u'ή',
                   u'Ἤ': u'ή',
                   u'Ἢ': u'ή',
                   u'Ἦ': u'ή',
                   u'ᾜ': u'ή',
                   u'ᾚ': u'ή',
                   u'ᾞ': u'ή',
                   u'ὴ': u'ή',
                   u'ῆ': u'ή',
                   u'ἤ': u'ή',
                   u'ἢ': u'ή',
                   u'ἦ': u'ή',
                   u'ῄ': u'ή',
                   u'ῂ': u'ή',
                   u'ῇ': u'ή',
                   u'ᾔ': u'ή',
                   u'ᾒ': u'ή',
                   u'ᾖ': u'ή',
                   u'Ἥ': u'ή',
                   u'Ἣ': u'ή',
                   u'Ἧ': u'ή',
                   u'ᾝ': u'ή',
                   u'ᾛ': u'ή',
                   u'ᾟ': u'ή',
                   u'ἣ': u'ή',
                   u'ἧ': u'ή',
                   u'ᾕ': u'ή',
                   u'ᾓ': u'ή',
                   u'ᾗ': u'ή',
                   u'Θ': u'θ',
                   u'Ι': u'ι',
                   u'Ἰ': u'ι',
                   u'ἰ': u'ι',
                   u'Ῑ': u'ι',
                   u'Ῐ': u'ι',
                   u'ῑ': u'ι',
                   u'ῐ': u'ι',
                   u'Ἱ': u'ι',
                   u'Ί': u'ί',
                   u'Ὶ': u'ί',
                   u'Ἴ': u'ί',
                   u'Ἲ': u'ί',
                   u'Ἶ': u'ί',
                   u'ὶ': u'ί',
                   u'ῖ': u'ί',
                   u'ἴ': u'ί',
                   u'ἲ': u'ί',
                   u'ἶ': u'ί',
                   u'Ἵ': u'ί',
                   u'Ἳ': u'ί',
                   u'Ἷ': u'ί',
                   u'ἳ': u'ί',
                   u'ἷ': u'ί',
                   u'Ϊ': u'ϊ',
                   u'ΐ': u'ϊ',
                   u'ῒ': u'ϊ',
                   u'ῗ': u'ϊ',
                   u'Κ': u'κ',
                   u'Λ': u'λ',
                   u'Μ': u'μ',
                   u'Ν': u'ν',
                   u'Ξ': u'ξ',
                   u'Ο': u'ο',
                   u'Ὀ': u'ο',
                   u'ὀ': u'ο',
                   u'Ὁ': u'ο',
                   u'Ό': u'ό',
                   u'Ὸ': u'ό',
                   u'Ὄ': u'ό',
                   u'Ὂ': u'ό',
                   u'ὸ': u'ό',
                   u'ὄ': u'ό',
                   u'ὂ': u'ό',
                   u'Ὅ': u'ό',
                   u'Ὃ': u'ό',
                   u'ὃ': u'ό',
                   u'Π': u'π',
                   u'Ρ': u'ρ',
                   u'Ῥ': u'ρ',
                   u'ῤ': u'ρ',
                   u'ῥ': u'ρ',
                   u'Σ': u'σ',
                   u'ς': u'σ',
                   u'Τ': u'τ',
                   u'Υ': u'υ',
                   u'ὐ': u'υ',
                   u'Ῡ': u'υ',
                   u'Ῠ': u'υ',
                   u'ῡ': u'υ',
                   u'ῠ': u'υ',
                   u'Ὑ': u'υ',
                   u'Ύ': u'ύ',
                   u'Ὺ': u'ύ',
                   u'ὺ': u'ύ',
                   u'ῦ': u'ύ',
                   u'ὔ': u'ύ',
                   u'ὒ': u'ύ',
                   u'ὖ': u'ύ',
                   u'Ὕ': u'ύ',
                   u'Ὓ': u'ύ',
                   u'Ὗ': u'ύ',
                   u'ὓ': u'ύ',
                   u'ὗ': u'ύ',
                   u'Ϋ': u'ϋ',
                   u'ΰ': u'ϋ',
                   u'ῢ': u'ϋ',
                   u'ῧ': u'ϋ',
                   u'Φ': u'φ',
                   u'Χ': u'χ',
                   u'Ψ': u'ψ',
                   u'Ω': u'ω',
                   u'Ὠ': u'ω',
                   u'ῼ': u'ω',
                   u'ᾨ': u'ω',
                   u'ὠ': u'ω',
                   u'ῳ': u'ω',
                   u'ᾠ': u'ω',
                   u'Ὡ': u'ω',
                   u'ᾩ': u'ω',
                   u'ᾡ': u'ω',
                   u'Ώ': u'ώ',
                   u'Ὼ': u'ώ',
                   u'Ὤ': u'ώ',
                   u'Ὢ': u'ώ',
                   u'Ὦ': u'ώ',
                   u'ᾬ': u'ώ',
                   u'ᾪ': u'ώ',
                   u'ᾮ': u'ώ',
                   u'ὼ': u'ώ',
                   u'ῶ': u'ώ',
                   u'ὤ': u'ώ',
                   u'ὢ': u'ώ',
                   u'ὦ': u'ώ',
                   u'ῴ': u'ώ',
                   u'ῲ': u'ώ',
                   u'ῷ': u'ώ',
                   u'ᾤ': u'ώ',
                   u'ᾢ': u'ώ',
                   u'ᾦ': u'ώ',
                   u'Ὥ': u'ώ',
                   u'Ὣ': u'ώ',
                   u'Ὧ': u'ώ',
                   u'ᾭ': u'ώ',
                   u'ᾫ': u'ώ',
                   u'ᾯ': u'ώ',
                   u'ὣ': u'ώ',
                   u'ὧ': u'ώ',
                   u'ᾥ': u'ώ',
                   u'ᾣ': u'ώ',
                   u'ᾧ': u'ώ'}
            safe = map.keys() + map.values()
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in map:
                    yield map[c]
                else:
                    yield c
        return ''.join(normalize_only_unsafe(string))


ell = ModernGreek