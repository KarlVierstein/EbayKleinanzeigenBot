import requests
import json

cookies = {
    'up': '%7B%22ln%22%3A%22606300982%22%2C%22lln%22%3A%229300df05-6423-4cce-b3e8-22e4cbd650d7%22%2C%22llstv%22%3A%2297-js-errorlog%3DA%7CBLN-18532_highlight%3DB%7CBLN-18275-lazy-load-image%3DA%7CDesktop_Test%3DB%7Creact-msgbox-payment-buy%3DB%7Creact-msgbox-payship%3DB%7CBLN-18685_auth_svr%3DA%7Cspeedcurve-labs-lux-1%3DB%7Cgdpr-experimental%3DC%7Cspeedcurve-labs-lux-2%3DB%7CBLN-18221_srp_rebrush_ads%3DB%7CBLN-18849-manage-ads-k8s%3DB%7C76-preact-header-footer%3DA%7CBLN-18727-TopAd-enabler%3DA%7C74-react-messagebox%3DA%7CEBAYKAD-2252_group-assign%3DA%22%2C%22ls%22%3A%22l%3D0%22%2C%22saSe%22%3A%22654913478%2C1339977246%2C-206938570%2C300235737%2C-3879627156%22%7D',
    'ioam2018': '0014660c08673577a60b8f62a:1653579178191:1622734378191:.ebay-kleinanzeigen.de:29:ebaykanz:ebayK-8:noevent:1622822846013:nioe0i',
    'iom_consent': '0103ff03ff&1622734382291',
    '_ga': 'GA1.2.1575819242.1622734379',
    '_gid': 'GA1.2.1579947978.1622734379',
    'clientId': '1575819242.1622734379',
    'ekConsentTcf2': '{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPHOZ3KPHOZ3KE1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABISADAAEDwg0AGAAIHhCIAMAAQPCFQAYAAgeEMgAwABA8IdABgACB4RCADAAEDwiUAGAAIHhFIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}',
    'ekConsentBucketTcf2': 'full2-exp',
    '__gads': 'ID=dd0634b32eb1c791:T=1622822550:S=ALNI_MYMP2CfUeufIdApdnhxwkPi739CcA',
    'overlayV21': 'seen',
    'wl': '%7B%22l%22%3A%221777769347%2C1569921%2C1325026%2C2411394%22%7D',
    'cto_bundle': '67Et4l9uUzRqZmlwTmVWT1k5ZEc3ZjB0ZHlPWG9iRzRXT2lVbjJwSUdjJTJCWW12RDFLREhVYjNTM0NSRTBQJTJGUlkyZ2hac29BJTJCZFFVNXFVaG9NVWdJeGRuYldPanZlVFRzZTRSYzJZTGoyZ0x6Y1ZZJTJCU3JzUWNneWdFN1kyVkI0UzRWZU5mbUNaOFVPUHZUSEJEZEVUWXlkcENjQjJBU1E3JTJCQUVPTzlrcGZCdFVSVEJmVExJNmJTVTRjOTk5NU1tSWxLOFBReHpQdlB0V0QwUGdSc2QydExRaDk3QSUzRCUzRA',
    'CSRF-TOKEN': 'c41e3601-f3dc-4c3b-8882-dc5414fad434',
    'GCLB': 'CKfHzPj_0JyyZg',
    'rbzid': '6Zd+zfSs390l0PQBftBLwBZlGONQE1Q7rW06JmlG/8whWfM15+QrOU9A+5eVsW9pg374daa1KnZkHAn5QukKeSyH8R0AffHFdw4juvX+ib3xMxNYZsrXy+hoqoMfP9aBAaGhc5ZrAc0WYjo6JTetvv3zRRCa+K6LdPoE8kDP5BEQs8Ws+bhC7/SPkwcg8OQxEqOVligCVmQ29frIc3yUp/Wi73iPZjeRAo5h6+EZSBw=',
    'rbzsessionid': '2b1c387a48c1511e526273b7d16636a5',
    'sc': '%7B%7D',
    'POPUPCHECK': '1622908021883',
    'JSESSIONID': 'ECBB9D3706F9C53AEE37180ABC7DFA49-mc2.koeb46-5_i01_1001',
}

headers = {
    'Host': 'www.ebay-kleinanzeigen.de',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': '*/*',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.ebay-kleinanzeigen.de/m-nachrichten.html',
    'Te': 'trailers',
    'Connection': 'close',
}

response = requests.get('https://www.ebay-kleinanzeigen.de/messagebox-api/view', headers=headers, cookies=cookies)
json_about_user = json.loads(response.content.decode("utf-8"))
bad_rating = json_about_user["ratingReasonsBad"]
good_rating = json_about_user["ratingReasonsGood"]
csrf_info = json_about_user["csrfToken"]
print(bad_rating)
