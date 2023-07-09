# 실행 argv: utf-8 strict 입력

import sys

스크립트, 입력_인코딩, error = sys.argv

def main(언어_파일, 인코딩, errors):
    줄 = 언어_파일.readline( )

    if 줄:
        줄_출력(줄, 인코딩, errors)
        return main(언어_파일, 인코딩, errors)

def 줄_출력(줄, 인코딩, errors):
    다음_언어 = 줄.strip( )
    생_바이트열 = 다음_언어.encode(인코딩, errors = errors)
    요리한_문자열 = 생_바이트열.decode(인코딩, errors = errors)

    print(생_바이트열, "<====>", 요리한_문자열)

언어들 = open("languages.txt", encoding="utf-8")

main(언어들, 입력_인코딩, error)

# C:\Users\pc\anaconda3\envs\learnPython3\python.exe C:/workspace/learnPython3/ex23/ex23.py utf-8 strict
# b'Afrikaans' <====> Afrikaans
# b'\xe1\x8a\xa0\xe1\x88\x9b\xe1\x88\xad\xe1\x8a\x9b' <====> አማርኛ
# b'\xd0\x90\xd2\xa7\xd1\x81\xd1\x88\xd3\x99\xd0\xb0' <====> Аҧсшәа
# b'\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xa9' <====> العربية
# b'Aragon\xc3\xa9s' <====> Aragonés
# b'Arpetan' <====> Arpetan
# b'Az\xc9\x99rbaycanca' <====> Azərbaycanca
# b'Bamanankan' <====> Bamanankan
# b'\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\x82\xe0\xa6\xb2\xe0\xa6\xbe' <====> বাংলা
# b'B\xc3\xa2n-l\xc3\xa2m-g\xc3\xba' <====> Bân-lâm-gú
# b'\xd0\x91\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f' <====> Беларуская
# b'\xd0\x91\xd1\x8a\xd0\xbb\xd0\xb3\xd0\xb0\xd1\x80\xd1\x81\xd0\xba\xd0\xb8' <====> Български
# b'Boarisch' <====> Boarisch
# b'Bosanski' <====> Bosanski
# b'\xd0\x91\xd1\x83\xd1\x80\xd1\x8f\xd0\xb0\xd0\xb4' <====> Буряад
# b'Catal\xc3\xa0' <====> Català
# b'\xd0\xa7\xd3\x91\xd0\xb2\xd0\xb0\xd1\x88\xd0\xbb\xd0\xb0' <====> Чӑвашла
# b'\xc4\x8ce\xc5\xa1tina' <====> Čeština
# b'Cymraeg' <====> Cymraeg
# b'Dansk' <====> Dansk
# b'Deutsch' <====> Deutsch
# b'Eesti' <====> Eesti
# b'\xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac' <====> Ελληνικά
# b'Espa\xc3\xb1ol' <====> Español
# b'Esperanto' <====> Esperanto
# b'\xd9\x81\xd8\xa7\xd8\xb1\xd8\xb3\xdb\x8c' <====> فارسی
# b'Fran\xc3\xa7ais' <====> Français
# b'Frysk' <====> Frysk
# b'Gaelg' <====> Gaelg
# b'G\xc3\xa0idhlig' <====> Gàidhlig
# b'Galego' <====> Galego
# b'\xed\x95\x9c\xea\xb5\xad\xec\x96\xb4' <====> 한국어
# b'\xd5\x80\xd5\xa1\xd5\xb5\xd5\xa5\xd6\x80\xd5\xa5\xd5\xb6' <====> Հայերեն
# b'\xe0\xa4\xb9\xe0\xa4\xbf\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xa6\xe0\xa5\x80' <====> हिन्दी
# b'Hrvatski' <====> Hrvatski
# b'Ido' <====> Ido
# b'Interlingua' <====> Interlingua
# b'Italiano' <====> Italiano
# b'\xd7\xa2\xd7\x91\xd7\xa8\xd7\x99\xd7\xaa' <====> עברית
# b'\xe0\xb2\x95\xe0\xb2\xa8\xe0\xb3\x8d\xe0\xb2\xa8\xe0\xb2\xa1' <====> ಕನ್ನಡ
# b'Kapampangan' <====> Kapampangan
# b'\xe1\x83\xa5\xe1\x83\x90\xe1\x83\xa0\xe1\x83\x97\xe1\x83\xa3\xe1\x83\x9a\xe1\x83\x98' <====> ქართული
# b'\xd2\x9a\xd0\xb0\xd0\xb7\xd0\xb0\xd2\x9b\xd1\x88\xd0\xb0' <====> Қазақша
# b'Krey\xc3\xb2l ayisyen' <====> Kreyòl ayisyen
# b'Latga\xc4\xbcu' <====> Latgaļu
# b'Latina' <====> Latina
# b'Latvie\xc5\xa1u' <====> Latviešu
# b'L\xc3\xabtzebuergesch' <====> Lëtzebuergesch
# b'Lietuvi\xc5\xb3' <====> Lietuvių
# b'Magyar' <====> Magyar
# b'\xd0\x9c\xd0\xb0\xd0\xba\xd0\xb5\xd0\xb4\xd0\xbe\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8' <====> Македонски
# b'Malti' <====> Malti
# b'\xe0\xa4\xae\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xa0\xe0\xa5\x80' <====> मराठी
# b'\xe1\x83\x9b\xe1\x83\x90\xe1\x83\xa0\xe1\x83\x92\xe1\x83\x90\xe1\x83\x9a\xe1\x83\xa3\xe1\x83\xa0\xe1\x83\x98' <====> მარგალური
# b'\xd9\x85\xd8\xa7\xd8\xb2\xd9\x90\xd8\xb1\xd9\x88\xd9\x86\xdb\x8c' <====> مازِرونی
# b'Bahasa Melayu' <====> Bahasa Melayu
# b'\xd0\x9c\xd0\xbe\xd0\xbd\xd0\xb3\xd0\xbe\xd0\xbb' <====> Монгол
# b'Nederlands' <====> Nederlands
# b'\xe0\xa4\xa8\xe0\xa5\x87\xe0\xa4\xaa\xe0\xa4\xbe\xe0\xa4\xb2 \xe0\xa4\xad\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa4\xbe' <====> नेपाल भाषा
# b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e' <====> 日本語
# b'Norsk bokm\xc3\xa5l' <====> Norsk bokmål
# b'Nouormand' <====> Nouormand
# b'Occitan' <====> Occitan
# b'O\xca\xbbzbekcha/\xd1\x9e\xd0\xb7\xd0\xb1\xd0\xb5\xd0\xba\xd1\x87\xd0\xb0' <====> Oʻzbekcha/ўзбекча
# b'\xe0\xa8\xaa\xe0\xa9\xb0\xe0\xa8\x9c\xe0\xa8\xbe\xe0\xa8\xac\xe0\xa9\x80' <====> ਪੰਜਾਬੀ
# b'\xd9\xbe\xd9\x86\xd8\xac\xd8\xa7\xd8\xa8\xdb\x8c' <====> پنجابی
# b'\xd9\xbe\xda\x9a\xd8\xaa\xd9\x88' <====> پښتو
# b'Plattd\xc3\xbc\xc3\xbctsch' <====> Plattdüütsch
# b'Polski' <====> Polski
# b'Portugu\xc3\xaas' <====> Português
# b'Rom\xc3\xa2n\xc4\x83' <====> Română
# b'Romani' <====> Romani
# b'\xd0\xa0\xd1\x83\xd1\x81\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9' <====> Русский
# b'Seeltersk' <====> Seeltersk
# b'Shqip' <====> Shqip
# b'Simple English' <====> Simple English
# b'Sloven\xc4\x8dina' <====> Slovenčina
# b'\xda\xa9\xd9\x88\xd8\xb1\xd8\xaf\xdb\x8c\xdb\x8c \xd9\x86\xd8\xa7\xd9\x88\xdb\x95\xd9\x86\xd8\xaf\xdb\x8c' <====> کوردیی ناوەندی
# b'\xd0\xa1\xd1\x80\xd0\xbf\xd1\x81\xd0\xba\xd0\xb8 / srpski' <====> Српски / srpski
# b'Suomi' <====> Suomi
# b'Svenska' <====> Svenska
# b'Tagalog' <====> Tagalog
# b'\xe0\xae\xa4\xe0\xae\xae\xe0\xae\xbf\xe0\xae\xb4\xe0\xaf\x8d' <====> தமிழ்
# b'\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb9\x84\xe0\xb8\x97\xe0\xb8\xa2' <====> ภาษาไทย
# b'Taqbaylit' <====> Taqbaylit
# b'\xd0\xa2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80\xd1\x87\xd0\xb0/tatar\xc3\xa7a' <====> Татарча/tatarça
# b'\xe0\xb0\xa4\xe0\xb1\x86\xe0\xb0\xb2\xe0\xb1\x81\xe0\xb0\x97\xe0\xb1\x81' <====> తెలుగు
# b'\xd0\xa2\xd0\xbe\xd2\xb7\xd0\xb8\xd0\xba\xd3\xa3' <====> Тоҷикӣ
# b'T\xc3\xbcrk\xc3\xa7e' <====> Türkçe
# b'\xd0\xa3\xd0\xba\xd1\x80\xd0\xb0\xd1\x97\xd0\xbd\xd1\x81\xd1\x8c\xd0\xba\xd0\xb0' <====> Українська
# b'\xd8\xa7\xd8\xb1\xd8\xaf\xd9\x88' <====> اردو
# b'Ti\xe1\xba\xbfng Vi\xe1\xbb\x87t' <====> Tiếng Việt
# b'V\xc3\xb5ro' <====> Võro
# b'\xe6\x96\x87\xe8\xa8\x80' <====> 文言
# b'\xe5\x90\xb4\xe8\xaf\xad' <====> 吴语
# b'\xd7\x99\xd7\x99\xd6\xb4\xd7\x93\xd7\x99\xd7\xa9' <====> ייִדיש
# b'\xe4\xb8\xad\xe6\x96\x87' <====> 中文