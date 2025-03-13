in_pth = r"C:\Users\tom_j\Downloads\AUCK00NZL_R_20250030000_01D_30S_MO.rnx\AUCK00NZL_R_20250030000_01D_30S_MO.rnx"
out_pth = r"C:\Users\tom_j\rin_read_out.txt"

lines = []
with open(in_pth) as f:
		obs_start = False
		for line in f:
				if "END OF HEADER" in line:
						for line in f:
								lines.append(line)

f.close()

with open(out_pth,"w") as f:
		f.write('\n'.join(str(i) for i in lines))
f.close()

