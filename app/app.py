from flask import Flask                    # 서버 구현을 위한 Flask 객체 import
from gensim.models import KeyedVectors

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
model = KeyedVectors.load_word2vec_format("ko_w2v_model") # 모델 로드

@app.route('/predict/<string:ko_word>', methods=['GET'])
def Predict(ko_word: str):
    global model    # 모델 전역 변수 선언

    try: # 모델에 단어 입력
        result = model.most_similar(ko_word)
        words = [word[0] for word in result]
        return {
            'status': 1,
            'result': words[:5]
        }
    except: # OOP 발생
        return {
            'status': 0,
            'result': 'Out Of Vocabulary'
        }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)