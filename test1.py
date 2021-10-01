from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.sidebar.title("streamlit 入門")
                 
st.write("ゆいこさん　こんばんは")

st.write("プログレスバーの表示")
"start!!"

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)
"done!!!!"

st.write("interactive widgets")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容書く")

text = st.sidebar.text_input("あなたの趣味を教えてください")
condition = st.sidebar.slider("あなたの今は調子は？", 0,100,50)

"あなたの趣味は", text
"コンディション:", condition

st.write("Display Image")



option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)

"あたなの好きな数字は", option, "です."






st.write("Dataframe")
df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})

st.table(df.style.highlight_max(axis=0))




df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ["lat","lon"]
)
st.map(df)









"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
