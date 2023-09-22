def linearSearchProduct(ProductList,
                        targetproduct):
   indices = []
  
   for index, product in enumerate(ProductList):
      if product == targetproduct:
       indices.append(index)
   return indices
#Example usage
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result = linearSearchProduct(products,target)
print(result)