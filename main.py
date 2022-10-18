# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import looker_sdk

sdk = looker_sdk.init40()
my_user = sdk.me()

print('Hola, estas entrando como: {} {}'.format(my_user["first_name"], my_user["last_name"]))


# Primero creamos el user attribute
sdk.create_user_attribute(
     body=looker_sdk.models40.WriteUserAttribute(
         name="attribute01",
         label="mylabel",
         type="string",
         user_can_view=True,
         value_is_hidden=False))

# Luego le damos un valor a este user attribute en mi caso le di "Falabella"
all_attributes = sdk.user_attribute_user_values(
    user_id=my_user.id)

# Revisamos a que id corresponde el atributo creado (ya que lo genera de forma aleatoria)
for attribute in all_attributes:
  print('user attribute id {} and value {} '.format(attribute.user_attribute_id, attribute.name))

# Luego con esta informacion le damos un valor a nuestro nuevo atributo.
user_id = my_user.id
attribute_id = "16"
attribute_value = "Falabella"
sdk.set_user_attribute_user_value(
    user_id=user_id,
    user_attribute_id=attribute_id,
    body=looker_sdk.models40.WriteUserAttributeWithValue(
        value=attribute_value))
