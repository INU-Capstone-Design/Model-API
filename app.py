from flask import Flask                    # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource      # Api 구현을 위한 Api 객체 import
from gensim.models import KeyedVectors

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)         # Flask 객체에 Api 객체 등록

@app.route('/<str:ko_word>')
class Model(Resource):
    def get(self, ko_word: str):
        global model    # 모델 전역 변수 선언

        try: # 모델에 단어 입력
            result = model.most_similar(ko_word)
            return {
                'status': 1,
                'result': result
            }
        except: # OOP 발생
            return {
                'status': 0,
                'result': 'Out Of Vocabulary'
            }

if __name__ == "__main__":
    model = KeyedVectors.load_word2vec_format("ko_w2v_model") # 모델 로드
    app.run(debug=True, port=80)