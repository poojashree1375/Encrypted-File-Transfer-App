
# File Transfer with Auto-Expiring Download Links

A simple and file-sharing system where users can upload a file and generate a unique download link that automatically expires after a selected time. All files are encrypted and stored safely, and deleted automatically after expiry.








## Features

Secure File Uploads – Uploaded files are encrypted before being stored.

Auto-Expiring Download Links – Each file is assigned a unique download link that automatically expires after the chosen time.

Client-Side Countdown Timer – Users can see a live countdown until the link expires.

Automatic File Deletion – Files are removed from the database once expired, keeping storage clean.

No File Storage on Server Disk – Files are processed in memory and stored only as encrypted bytes.

Copy-to-Clipboard Link Button – Users can easily copy the generated download link.

Clean & Modern UI – Uses a glassmorphism-styled interface with glowing buttons.

Simple & Lightweight – No login, no unnecessary steps—just upload, get link, and share.

Error Handling – If a link is invalid or expired, a dedicated “Expired” page is shown.


## Tech Stack

**Backend**: Python, Django, SQLite(Development Database)

**Security**: Cryptography(Fernet Encryption), Hahed tokens

**Frontend**: HTML, CSS, JavaScript(Countdown and Copy button)

**Tools**: Git and GitHub, Virtual Environment(venv)



## Screenshots

###Upload Page<img width="1918" height="1133" alt="Screenshot 2025-11-30 114309" src="https://github.com/user-attachments/assets/e01abbf8-154e-4e74-9d2d-9d9df2ec73ef" />

###Upload Page<img width="1919" height="1137" alt="Screenshot 2025-11-30 115149" src="https://github.com/user-attachments/assets/c60505be-db47-46fa-b6ac-759296b9b4f7" />

###Download Link Page<img width="1919" height="1133" alt="Screenshot 2025-11-30 115204" src="https://github.com/user-attachments/assets/4ec9ea97-39c2-4747-922b-17230f196a31" />

###Download Link Page<img width="1919" height="1136" alt="Screenshot 2025-11-30 115219" src="https://github.com/user-attachments/assets/a4722632-385b-4a62-87d4-565cd1f8d4cf" />

###Downloading file<img width="1913" height="1117" alt="Screenshot 2025-11-30 115246" src="https://github.com/user-attachments/assets/5c0297d0-d280-4555-8c0f-31d8b5bde787" />

###File downloaded<img width="1916" height="1134" alt="Screenshot 2025-11-30 115257" src="https://github.com/user-attachments/assets/4b60e243-a3d6-4d54-ba1c-2a979ad57874" />

###Download Link expired<img width="1919" height="1138" alt="Screenshot 2025-11-30 115345" src="https://github.com/user-attachments/assets/2eb8d3d9-4306-4587-a132-4ee0afe4a583" />

###Downloading File<img width="1913" height="1117" alt="Screenshot 2025-11-30 115246" src="https://github.com/user-attachments/assets/1425fd1e-5513-4bb1-a64f-b550f13a2e77" />

###Expired Link Page<img width="1919" height="1137" alt="Screenshot 2025-11-30 115332" src="https://github.com/user-attachments/assets/25a297b8-8034-42ba-8a82-af69737f41da" />

##Demo
https://github.com/poojashree1375/File-Transfer-with-Auto-Expiring-Download-Links/commit/bdac62f2c70911973a90bd3179acb28da9575648







