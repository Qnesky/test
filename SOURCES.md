# Откуда скачан каждый исходный файл

База Росстата: `https://rosstat.gov.ru/storage/mediabank/<имя>`. Сертификат сайта выпущен Russian Trusted CA (Минцифры); корневой и промежуточный сертификаты взяты с gu-st.ru и nuc-cdp.digital.gov.ru, проверка TLS не отключалась.

| Папка / файл | URL |
|---|---|
| 01: Invest_sub_2000-2025.xlsx, Invest_vsego_2025.xls, Inv_reg_kv_2020_2026.xlsx, Inv_reg_ksr_1pg-2026.xls, met-inv-fed.pdf, met-inv-reg.rar | rosstat.gov.ru/storage/mediabank/… (страница https://rosstat.gov.ru/investment_nonfinancial) |
| 01: met-ok.pdf | rosstat.gov.ru/storage/mediabank/xoCyl4Ia/met-ok.pdf |
| 02: regiony_rossii_razdel_investicii/RR20XX_* | разделы из архивов «Регионы России. Социально-экономические показатели» (https://rosstat.gov.ru/folder/210/document/13204): Region_Pokaz_2025.rar, Region_Pokaz_2024.rar, Region_Pokaz_2023.rar, Region_Pokazateli_2022.rar, soc_pok_2021.rar, 3kXY2H0y/soc_pok_2020.rar, soc-pok2019.rar, soc-pok18.rar, soc-pok17.rar, soc-pok2016.rar, soc-pok2015.rar, soc-pok(5).rar [2014], soc-pok(4).rar [2013], soc-pok(3).rar [2012], soc-pok(2).rar [2011], soc-pok(1).rar [2010] |
| 03: Inv_OKVED2_2025.xls, Din_OKVED2_2025.xls, met-din.pdf | rosstat.gov.ru/storage/mediabank/… (страница investment_nonfinancial) |
| 04: rosstat_MSP_prilozhenie_gospodderzhka/*.xls | из архивов приложений к «Малое и среднее предпринимательство в России» (https://rosstat.gov.ru/folder/210/document/13223), см. 07 |
| 05: Din_invest_sub.xlsx, Din_invest_vsego_2025.xls | rosstat.gov.ru/storage/mediabank/… |
| 06: cbr_*.xml | https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2009&date_req2=31/12/2024&VAL_NM_RQ=R01235 (USD), R01239 (EUR) |
| 06: EIA_RBRTEa/m/d | https://www.eia.gov/dnav/pet/hist_xls/RBRTEa.xls (m, d аналогично) |
| 06: CMO-Historical-Data-Annual.xlsx | https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Annual.xlsx |
| 06: rosstat_VRP/* | rosstat.gov.ru/storage/mediabank/VRP_OKVED2007.xlsx, VRP_OKVED2_s_2016.xlsx, VRP_s1998.xlsx (страница https://rosstat.gov.ru/statistics/accounts) |
| 07: rosstat_MSP_v_Rossii/*.rar | Pril_Mal_pred_2024.rar, pril_mal_pred_2022.rar, pril-mal-pred19.rar, pril-mal-pred.rar [2017], mal-pred-all(2).rar [2015], mal-pred-all(1).rar [2014], mal-pred-all.rar [2013], mal-sp-pred(1).rar [2012], mal-sp-pred.rar [2010] |
| 07: fns_rmsp_statistics_json/*.json | POST https://rmsp.nalog.ru/statistics-proc.json, statDate=ДД.ММ.ГГГГ&level=1&fo=1 (тот же запрос делает страница https://rmsp.nalog.ru/statistics.html) |
| 08: pravo_gov_ru_official_pdf/*.pdf | http://publication.pravo.gov.ru/file/pdf?eoNumber=<номер>; номера: 0001201404240014 (316), 0001201405270007 (482), 0001201501080020 (1605), 0001201902120005 (110), 0001201905240033 (638), 0001201910090011 (1284), 0001202005120012 (646), 0001202010060012 (1563), 0001202010060014 (1572), 0001202012210028 (2105), 0001202012220046 (2154), 0001202111240006 (1998), 0001202203240005 (413), 0001202203290024 (491), 0001202212060029 (2217), 0001202304270003 (657), 0001202308140022 (1324) |
| 08: garant_* | https://www.garant.ru/products/ipo/prime/doc/<id>/ : 12065680 (ПП 178), 70094890 (654), 71196256 (1452), 72070692 (110), 72726270 (1284), 403646478 (413), 403680608 (491), 406702361 (657), 407423583 (1324); https://base.garant.ru/70644224/ (ПП 316, действующая редакция) |
| 08: consultant_PP178_red2014 | https://www.consultant.ru/document/cons_doc_LAW_85598/ и его разделы |
| 10: garant_prime_html/* | https://www.garant.ru/products/ipo/prime/doc/<id>/ : 12076730, 70111094, 70232844, 70526136, 70633846, 70829534, 71041192, 71246336, 71499854, 71859428, 72191798, 72701678, 71224418 |
