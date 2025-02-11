'''선물옵션 종목코드(fo_stk_code_mts.mst) 정제 파이썬 파일'''

import pandas as pd
import urllib.request
import ssl
import zipfile
import os

def get_domestic_stk_future_master_dataframe(base_dir):
    
    # download file
    print("Downloading...")

    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve("https://new.real.download.dws.co.kr/common/master/fo_stk_code_mts.mst.zip", base_dir + "fo_stk_code_mts.mst.zip")
    #os.chdir(base_dir)

    fo_stk_code_zip = zipfile.ZipFile(base_dir + 'fo_stk_code_mts.mst.zip')
    fo_stk_code_zip.extractall(base_dir)
    fo_stk_code_zip.close()
    file_name = base_dir + "fo_stk_code_mts.mst"

    fo_stk_code_zip = zipfile.ZipFile(base_dir + 'fo_stk_code_mts.mst.zip')
    fo_stk_code_zip.extractall(base_dir)
    fo_stk_code_zip.close()
    file_name = base_dir + "fo_stk_code_mts.mst"

    columns = ['상품종류','단축코드','표준코드',' 한글종목명',' ATM구분',
               ' 행사가',' 월물구분코드',' 기초자산 단축코드',' 기초자산 명']
    df=pd.read_table(file_name, sep='|',encoding='cp949',header=None)
    df.columns = columns
    df.to_excel(base_dir + 'fo_stk_code_mts.xlsx',index=False)  # 현재 위치에 엑셀파일로 저장

    return df
    
if __name__ == "__main__":
    # 다운로드 및 저장 디렉토리 설정
    base_dir = os.getcwd() + "\\data\\"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    df = get_domestic_stk_future_master_dataframe(base_dir)
    print("Done")
    