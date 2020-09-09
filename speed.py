from speedtest import Speedtest

st = Speedtest()

print('Shovit Roy! Your Download speed is ', st.download()/1024/1024)
print('Shovit Roy ! Your upload speed is ', st.upload()/1024/1024)