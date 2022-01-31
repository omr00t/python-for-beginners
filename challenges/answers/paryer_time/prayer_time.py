# https://www.mara.gov.om/calendar_page4.asp
import sys
import urllib.request

PRAYERS = ("Fajr", "Shorouk", "Dhuhr", "Asr", "Maghrib", "Isha")

def get_today_prayer_times(city):
    res = urllib.request.urlopen("https://www.mara.gov.om/calendar_page4.asp")
    html = res.read()
    city_offset = html.find(city.encode())
    end_tr_tag_index = html.find(b"</tr>", city_offset)
    
    prayer_data = html[city_offset:end_tr_tag_index]
    prayer_list = prayer_data.split(b"</td><td>")

    assert city == prayer_list[0].decode(), "Failed parsing data!"

    print(city)

    print("\t" + f"{'Prayer':8}   Time")
    print("\t" + "-"*16)
    for i in range(len(PRAYERS)):
        print("\t" + f"{PRAYERS[i]:8} : {prayer_list[i+1].strip(b'</td>').decode()}")

def main():
    if(len(sys.argv) != 2):
        print(f"python {sys.argv[0]} <city>")
        print(f"python {sys.argv[0]} Bidiya")
        sys.exit(0)

    get_today_prayer_times(sys.argv[1])

if __name__ == "__main__":
    main()
