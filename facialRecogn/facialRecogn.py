# 导入所需的库
import wasmtime

engine = wasmtime.Engine()
store = wasmtime.Store(engine)
module = wasmtime.Module(store.engine, 'aleo_zk_algorithm.wasm')
instance = wasmtime.Instance(module, [])

# 调用函数
result = instance.exports.my_algorithm(0)

