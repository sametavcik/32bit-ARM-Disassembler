# 32bit-ARM-Disassembler

## Bu proje, 32 bitlik Makine kodunu belirli yönergeler dahilinde ARM Assembly diline çevirmeyi yani reverse engineering ile [Disassembler](https://en.wikipedia.org/wiki/Disassembler) yapmayı amaçlamaktadır.
#### ARM Assembly dili tanıtımı
* [arm-assembly.pdf](https://github.com/sametavcik/32bit-ARM-Disassembler/files/9710127/06.arm-assembly.pdf)
* [machine-lang.pdf](https://github.com/sametavcik/32bit-ARM-Disassembler/files/9710133/07.machine-lang.pdf)


#### Proje sadece aşağıdaki yönergeler baz alınarak hazırlanmıştır.

## Data Processing Instructions
![Adsız7](https://user-images.githubusercontent.com/65908597/193911720-8ff6d613-0602-48eb-8e4e-22d52bca3306.png)
![Adsız8](https://user-images.githubusercontent.com/65908597/193911732-0a266b51-27ba-4839-b5ec-8a78927f6e37.png)

## Memory Instructions
![Adsız9](https://user-images.githubusercontent.com/65908597/193912915-286a1b91-4157-4589-bff3-d2ff3f36d48c.png)

## Branch Instructions
![Adsız10](https://user-images.githubusercontent.com/65908597/193913253-b6b9c61d-ee31-423b-801c-4f398183b2f9.png)

## Condition Instructions
![Adsız11](https://user-images.githubusercontent.com/65908597/193913543-8cf6f9f5-d90a-4ffe-87f1-451e30091f20.png)

## INPUTS
* Makine kodları 8 byte'lık hexadecimal ve '0x' kısmı atılmış şekilde girilmektedir.(örn: kod 0xE086500 ise E086500 şeklinde girilmeli)


![Adsız12](https://user-images.githubusercontent.com/65908597/193915781-5f419106-b600-4e2a-b1ab-82f49a043e2a.png)

## OUTPUTS

![Adsız13](https://user-images.githubusercontent.com/65908597/193918476-82222ee4-654f-454a-adce-9b26d4e77678.png)

# Data Processing Examples
### 1-) Immediate Example
***


![Adsız14](https://user-images.githubusercontent.com/65908597/193919977-a30a65fc-0756-4b32-93d5-2f4404e5f602.png)

![Adsız15](https://user-images.githubusercontent.com/65908597/193920546-7f8599de-6db1-4735-be1e-2c8fe3b2b584.png)

#### OUTPUTS

![Adsız16](https://user-images.githubusercontent.com/65908597/193921029-17a38397-a73a-4337-8d7c-ce033cf3e75e.png)

### 2-) Register Example
***

![Adsız17](https://user-images.githubusercontent.com/65908597/193923378-df972ff2-ccfd-43f1-9808-626ac5ba799b.png)

![Adsız18](https://user-images.githubusercontent.com/65908597/193924898-49b743ed-c160-4376-93ba-a87093c651a0.png)

#### OUTPUTS

![Adsız19](https://user-images.githubusercontent.com/65908597/193925030-1acb1899-fec2-49ca-85d4-e5791258ccbf.png)


### 3-) Register Shifted Register Example
***
![Adsız21](https://user-images.githubusercontent.com/65908597/193928310-3d48b916-6703-4df9-a24e-832e41077e3c.png)


![Adsız20](https://user-images.githubusercontent.com/65908597/193927820-555c0bfc-41f4-4097-90d0-c0e3b4f176f0.png)

#### OUTPUTS
![Adsız22](https://user-images.githubusercontent.com/65908597/193928589-ea189ffb-4a5e-4419-a02b-142d7103ad64.png)






