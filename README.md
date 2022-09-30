# fearAndGreed 更新到 google spreadsheet

- 前置作業  
	- 記下 google spreadsheet url 裡面的 sheet key 
	- 在 [google api console](https://console.cloud.google.com/apis/dashboard) 要有一個專案，沒有的話要新增  
	- ENABLE APIS AND SERVICES 按鈕，啟用Google Sheets API  
	- Credentials  
		- Create service account  
		- 在 service accoun ID 新增 ID  
		- Create and Continue  
		- Select a role => editor  
		- 將 service account email (或在憑證 JSON 裡面也有) 加入 sheet share 共用，給予 editor 權限  
		- 點擊 keys => create new key => JSON  