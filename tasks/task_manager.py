import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore
from sklearn.utils import resample

# Açıklama: CSV dosyasından veriyi pandas DataFrame olarak oku.
# Input: "death_note_characters.csv"
# Output: pandas.DataFrame
# Kolonlar örneği: ['name', 'iq', 'aggression', 'justice_score', 'city', 'is_suspect']
def load_character_data(path: str) -> pd.DataFrame:
    pass

# Açıklama: Tüm kolon adlarını küçük harfe çevir ve boşlukları alt çizgiyle değiştir.
# Input: pd.DataFrame(columns=["Name", "Justice Score", "Is Suspect"])
# Output: pd.DataFrame(columns=["name", "justice_score", "is_suspect"])
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    pass


# Açıklama: Belirtilen sütundaki eksik değerleri ortalama ile doldur.
# Input: "justice_score"
# Output: Null değerler ortalama ile doldurulmuş DataFrame
def fill_missing_scores(df: pd.DataFrame, column: str) -> pd.DataFrame:
    pass

# Açıklama: city sütununu one-hot encode et.
# Input: "tokyo", "kyoto", "osaka"
# Output: city_tokyo, city_kyoto, city_osaka sütunları
def encode_city_column(df: pd.DataFrame) -> pd.DataFrame:
    pass

# Açıklama: iq sütunundaki z-skoru 3'ten büyük olanları tespit et ve ayrı bir sütunda “is_outlier” olarak işaretle.
# Output: Yeni sütun: is_outlier (True/False)
def detect_outliers_iq(df: pd.DataFrame) -> pd.DataFrame:
    pass

# Açıklama: aggression sütununu min-max normalizasyon ile 0-1 arasına getir.
# Output: Yeni sütun: aggression_scaled
def scale_aggression(df: pd.DataFrame) -> pd.DataFrame:
    pass

# Açıklama: Aşağıdaki şekilde bir “suspect_score” oluştur:
# Formül: df['suspect_score] = 0.4 * df['iq'] + 0.6 * df['aggresion_scaled]
def generate_suspect_score(df: pd.DataFrame) -> pd.DataFrame:
    pass


# Açıklama: is_suspect == 1 olanları resample ederek sayıca is_suspect == 0 kadar yap.
def upsample_suspects(df: pd.DataFrame) -> pd.DataFrame:
    pass

# Açıklama: Suspect score’a göre en yüksek n kişiyi getir.
# Input: n = 5
# Output: İlk 5 kişi (yüksekten düşüğe sıralı)
def get_top_suspects(df: pd.DataFrame, n: int) -> pd.DataFrame:
    pass

# Açıklama: Temizlenmiş ve puanlanmış veriyi CSV’ye yaz.
def export_results(df: pd.DataFrame, path: str) -> None:
    pass