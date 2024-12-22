import sys
import pandas as pd

def load_data(file_path):
    # تحميل البيانات من الملف المحدد
    df = pd.read_csv(file_path)
    # حفظ البيانات للخطوة التالية
    df.to_csv('initial_df.csv', index=False)
    
    # استدعاء السكربت التالي
    import dpre
    dpre.process_data('initial_df.csv')

if __name__ == "__main__":
    # قم بتمرير المسار مباشرة كمعامل للدالة
    load_data(r"winter_data.csv")


