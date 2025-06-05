import speedtest
import pandas as pd
from datetime import datetime
import os


def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "Timestamp": timestamp,
        "Download (Mbps)": round(download_speed, 2),
        "Upload (Mbps)": round(upload_speed, 2),
        "Ping (ms)": round(ping, 2)
    }


def save_to_csv(data, filename="internet_speed_report.csv"):
    df = pd.DataFrame([data])
    if not os.path.exists(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)


def main():
    print("📶 Measuring internet speed...")
    result = run_speed_test()
    print(f"\n📊 Result:\nDownload: {result['Download (Mbps)']} Mbps\nUpload: {result['Upload (Mbps)']} Mbps\nPing: {result['Ping (ms)']} ms\nTime: {result['Timestamp']}")
    save_to_csv(result)
    print("✅ Report saved to 'internet_speed_report.csv'.")

if __name__ == "__main__":
    main()
