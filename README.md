# 取得所需要的資料 access_token , zone_id , record_id

## 申請domain的Access Token
>
>先登入[Cloudflare](https://dash.cloudflare.com/)
>
>右上角的人頭按下去，找到我的設定檔
>
><img width="315" alt="1" src="https://github.com/user-attachments/assets/90c024e6-25fc-4287-90f0-630d2434fc87" />
>
>左邊選項列選 API權杖
>
><img width="203" alt="2" src="https://github.com/user-attachments/assets/586d6ddb-d284-4dc7-a198-7775cfad1955" />
>
>點選建立Token
>
><img width="679" alt="3" src="https://github.com/user-attachments/assets/453e648e-9a59-4a15-872d-cea0b96234ff" />
>
>找到編輯區域DNS，點選使用範本
>
><img width="561" alt="4" src="https://github.com/user-attachments/assets/27714dae-b020-4d15-9390-bc76380d96e4" />
>
>將資料填上，並點擊下方的繼續至摘要
>
><img width="463" alt="5" src="https://github.com/user-attachments/assets/ca13ab7d-3b06-4b54-a36a-4de7bf84f937" />
>
>沒問題就可以點選建立Token囉
>
><img width="448" alt="6" src="https://github.com/user-attachments/assets/a812c2a6-2f9f-4b32-a6b4-9d41f8bf48d7" />
>
>最後拿黑底裡的command測試看看
>
><img width="710" alt="7" src="https://github.com/user-attachments/assets/100a9fd6-daba-4eaa-994a-44b5be53fa77" />
>
>若成功會出現
>
><img width="950" alt="8" src="https://github.com/user-attachments/assets/fa8a75f3-d909-49ba-b043-7229eba85303" />
>
>看起來非常難閱讀
>
>可以嘗試在 command最後面加上 ```| python3 -m json.tool``` 轉成json格式輸出
>
><img width="430" alt="9" src="https://github.com/user-attachments/assets/442cf2cb-4a5c-4664-b8f2-4a05436672a9" />
>
>看起來就相當好閱讀囉(開記事本先把token記起來)
>
>
## 取得zoneID
>
>將
```
token=剛剛拿到的token
curl -X GET "https://api.cloudflare.com/client/v4/zones" \
  -H "Authorization: Bearer ${token}" \
  -H "Content-Type:application/json" | python3 -m json.tool
```
>貼到terminal裡，會得到ZoneID(開記事本先把zoneID記起來)
>
><img width="569" alt="10" src="https://github.com/user-attachments/assets/a8a9dbe6-128e-4b11-85f1-4b8d8f39a715" />
>
>
## 取得recordID
>zoneID=剛剛拿到的zoneID
>
>將
```
zoneID=剛剛拿到的zoneID
curl -X GET "https://api.cloudflare.com/client/v4/zones/${zoneID}/dns_records" \
  -H "Authorization: Bearer ${token}" \
  -H "Content-Type:application/json" | python3 -m json.tool
```
>貼到terminal裡，會得到recordID(開記事本先把recordID記起來)
>
><img width="400" alt="11" src="https://github.com/user-attachments/assets/62328d64-ffb5-4fbc-a27e-1f8c2f7dbb70" />







