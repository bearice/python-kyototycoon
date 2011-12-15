kt = __kyototycoon__
db = kt.db
-- echo back the input data as the output data
function echo(inmap, outmap)
   for key, value in pairs(inmap) do
      outmap[key] = value
   end
   return kt.RVSUCCESS
end

