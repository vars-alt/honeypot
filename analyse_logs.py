import pandas as pd

df = pd.read_csv('honeypot_log.csv', names=['timestamp','ip','port'])
print("Total attempts:", len(df))
top_ips = df['ip'].value_counts().head(3)
top_ports = df['port'].value_counts()
print("Top IPs:\n", top_ips)
print("Top ports:\n", top_ports)

# Export to Excel
df.to_excel('honeypot_summary.xlsx', index=False)
