import sys
from interface import app
from utils.fn import trace_calls

if __name__ == '__main__':
    # sys.settrace(trace_calls) # 监视运行状态
    app.run(debug=True, port=8080)
