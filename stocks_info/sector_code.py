import pandas as pd
import urllib.request
import ssl
import zipfile
import os

def get_sector_master_dataframe(base_dir):

    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve("https://new.real.download.dws.co.kr/common/master/idxcode.mst.zip", base_dir + "idxcode.zip")
    #os.chdir(base_dir)

    idxcode_zip = zipfile.ZipFile(base_dir + 'idxcode.zip')
    idxcode_zip.extractall(base_dir)
    idxcode_zip.close()

    file_name = base_dir + "idxcode.mst"
    df = pd.DataFrame(columns = ['업종코드', '업종명'])

    ridx = 1
    with open(file_name, mode="r", encoding="cp949") as f:
        for row in f:
            tcode = row[1:5]  # 업종코드 4자리 (맨 앞 1자리 제거)
            tname = row[3:43].rstrip() #업종명
            df.loc[ridx] = [tcode, tname]
            # print(df.loc[ridx])  # 파일 작성중인 것을 확인할 수 있음
            ridx += 1

    return df

if __name__ == "__main__":
    # 다운로드 및 저장 디렉토리 설정
    base_dir = os.getcwd() + "\\data\\"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    df2 = get_sector_master_dataframe(base_dir)
    df2.to_excel(base_dir + 'idxcode.xlsx',index=False) # 현재 위치에 엑셀파일로 저장
    df2
