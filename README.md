# Land-Price-API

[Software Testing Final Project] This API provides data for lands, their widths, lengths, prices, and tax. 

## Team Members

| Name | NIM |
|------|-----|
|[Difta Fitrahul Qihaj](https://github.com/DiftaFitrahul) | 21/480096/TK/52975 |
|[Ahmad Zaki Akmal](https://github.com/ahmadzakiakmal) | 21/480179/TK/52981 |
|[Raditya Christoaji B. P.](https://github.com/Rexiar) | 21/481218/TK/53115 |

## Endpoints

### 1. Get Land
| | |
|-|-|
|Method       | `GET` |
|URL          | `/land/<id>` |
|Description  | Gets information about a land |
|Params       | `id` |
|Body         | none |

### 2. Add Land
| | |
|-|-|
|Method       | `POST` |
|URL          | `/land/` |
|Description  | Registers a new land |
|Params       | none |
|Body         | `{city, width, length, local_price_per_area, tax_per_area }` |

## 3. Edit Land
| | |
|-|-|
|Method       | `PUT` |
|URL          | `/land/<id>` |
|Description  | Edits an existing land |
|Params       | `id` |
|Body         | `{city, width, length, local_price_per_area, tax_per_area }` |

## 4. Delete Land
| | |
|-|-|
|Method       | `DELETE` |
|URL          | `/land/<id>` |
|Description  | Deletes a land |
|Params       | `id` |
|Body         | none |

## 5. Calculate Land Area
| | |
|-|-|
|Method       | `GET` |
|URL          | `/land/area/<id>` |
|Description  | Calculates the area of a land |
|Params       | `id` |
|Body         | none |

## 6. Calculate Land Price
| | |
|-|-|
|Method       | `GET` |
|URL          | `/land/price/<id>` |
|Description  | Calculates the total price of a land |
|Params       | `id` |
|Body         | none |

## 7. Calculate Land Tax
| | |
|-|-|
|Method       | `GET` |
|URL          | `/land/tax/<id>` |
|Description  | Calculates the tax of a land |
|Params       | `id` |
|Body         | none |