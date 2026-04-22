# Substrate parser eval — 50-verse hand-review sheet

**Goal:** verify that the multitask (ByT5) parser is ≥95% correct at the lemma level.

**How to use:** Skim each verse. For every multitask row that is WRONG, write `✗` next to it (in the same line, after a `→` arrow). If the lemma is right but the morph is wrong, write `morph:✗`. If everything is right, do nothing — that's the default. The vidyut column is shown only as a sanity contrast — ignore for scoring.

**Conventions:** lemma in IAST, morphology in human English. Compound members marked `compound (compound member)` are correctly tagged when they're indeed compound elements.

**Total verses:** 50 · **multitask tokens:** 756 · **vidyut tokens:** 822

---


## BG 1.16 — Arjuna

**Devanāgarī:** अनन्त-विजयं राजा कुन्ती-पुत्रो युधिष्ठिरः | नकुलः सहदेवश् च सुघोष-मणिपुष्पकौ

**IAST:** *ananta-vijayaṃ rājā kuntī-putro yudhiṣṭhiraḥ | nakulaḥ sahadevaś ca sughoṣa-maṇipuṣpakau*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | ananta | **ananta** | compound (compound member) | _añji_ |
| 1 | vijayam | **vijaya** | accusative masculine singular noun | _anti_ |
| 2 | rājā | **rājan** | nominative masculine singular noun | _—_ |
| 3 | kuntī | **kuntī** | compound (compound member) | _viji_ |
| 4 | putraḥ | **putra** | nominative masculine singular noun | _rāj_ |
| 5 | yudhiṣṭhiraḥ | **yudhiṣṭhira** | nominative masculine singular noun | _kunti_ |
| 6 | nakulaḥ | **nakula** | nominative masculine singular noun | _—_ |
| 7 | sahadevaḥ | **sahadeva** | nominative masculine singular noun | _—_ |
| 8 | ca | **ca** | — | _yudhiṣṭhira_ |
| 9 | sughoṣa | **sughoṣa** | compound (compound member) | _nakula_ |
| 10 | maṇipuṣpakau | **maṇipuṣpaka** | nominative masculine dual noun | _sahadeva_ |
| 11 | ca | **—** | — | _ca `vocative singular masculine noun`_ |
| 12 | sughoṣa | **—** | — | _sughoṣa_ |
| 13 | - | **—** | — | _—_ |
| 14 | maṇipuṣpakau | **—** | — | _maṇipuṣpaka_ |


## BG 1.46 — Arjuna

**Devanāgarī:** यदि माम् अप्रतीकारम् अशस्त्रं शस्त्र-पाणयः | धार्तराष्ट्रा रणे हन्युस् तन् मे क्षेमतरं भवेत्

**IAST:** *yadi mām apratīkāram aśastraṃ śastra-pāṇayaḥ | dhārtarāṣṭrā raṇe hanyus tan me kṣemataraṃ bhavet*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | yadi | **yadi** | — | _yadi_ |
| 1 | mām | **mad** | accusative singular noun | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 2 | apratīkāram | **apratīkāra** | accusative masculine singular noun | _aprati_ |
| 3 | aśastram | **aśastra** | accusative masculine singular noun | _īkāra_ |
| 4 | śastra | **śastra** | compound (compound member) | _aśastra_ |
| 5 | pāṇayaḥ | **pāṇi** | nominative masculine plural noun | _śastra_ |
| 6 | dhārtarāṣṭrāḥ | **dhārtarāṣṭra** | nominative masculine plural noun | _—_ |
| 7 | raṇe | **raṇa** | locative masculine singular noun | _—_ |
| 8 | hanyuḥ | **han** | present optative 3rd person plural verb | _dhā_ |
| 9 | tat | **tad** | nominative neuter singular noun | _ṛ `vocative singular masculine noun`_ |
| 10 | me | **mad** | genitive singular noun | _a `vocative singular masculine noun`_ |
| 11 | kṣemataram | **kṣematara** | nominative neuter singular noun | _aś `instrumental singular masculine noun`_ |
| 12 | bhavet | **bhū** | present optative 3rd person singular verb | _raṇ_ |
| 13 | ī | **—** | — | _i `nominative dual masculine noun`_ |
| 14 | hanyus | **—** | — | _han_ |
| 15 | tan | **—** | — | _tan_ |
| 16 | me | **—** | — | _mā `locative singular neuter noun`_ |
| 17 | kṣā | **—** | — | _kṣā_ |
| 18 | im | **—** | — | _i `accusative singular masculine noun`_ |
| 19 | ataram | **—** | — | _tṝ_ |
| 20 | bhavet | **—** | — | _bhū_ |


## BG 2.12 — Krishna

**Devanāgarī:** कुतस् ते अशोच्याः ? यतो नित्याः | कथम् ? न त्व् एवाहं जातु नासं न त्वं नेमे जनाधिपाः | न चैव न भविष्यामः सर्वे वयम् अतः परम्

**IAST:** *kutas te aśocyāḥ ? yato nityāḥ | katham ? na tv evāhaṃ jātu nāsaṃ na tvaṃ neme janādhipāḥ | na caiva na bhaviṣyāmaḥ sarve vayam ataḥ param*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | kutas | **kutas** | — | _ku `nominative plural masculine noun`_ |
| 1 | te | **tad** | nominative masculine plural noun | _tā `nominative dual feminine noun`_ |
| 2 | aśocyāḥ | **aśocya** | nominative masculine plural noun | _śuc_ |
| 3 | yatas | **yatas** | — | _a `nominative plural masculine noun`_ |
| 4 | nityāḥ | **nitya** | nominative masculine plural noun | _yat_ |
| 5 | katham | **katham** | — | _nitya_ |
| 6 | na | **na** | — | _katham_ |
| 7 | tu | **tu** | — | _na `vocative singular neuter noun`_ |
| 8 | eva | **eva** | — | _tu `nominative singular masculine noun`_ |
| 9 | aham | **mad** | nominative singular noun | _eva_ |
| 10 | jātu | **jātu** | — | _ha `accusative singular masculine noun`_ |
| 11 | na | **na** | — | _jātu_ |
| 12 | āsam | **as** | impf indicative 1st person singular | _na `nominative plural masculine noun`_ |
| 13 | na | **na** | — | _a `accusative singular masculine noun`_ |
| 14 | tvam | **tvad** | nominative singular noun | _na `vocative singular neuter noun`_ |
| 15 | na | **na** | — | _tva_ |
| 16 | ime | **idam** | nominative masculine plural noun | _nema_ |
| 17 | janādhipāḥ | **janādhipa** | nominative masculine plural noun | _janādhipa_ |
| 18 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 19 | ca | **ca** | — | _ca `vocative singular masculine noun`_ |
| 20 | eva | **eva** | — | _eva_ |
| 21 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 22 | bhaviṣyāmaḥ | **bhū** | future indicative 1st person plural verb | _bhū_ |
| 23 | sarve | **sarva** | nominative masculine plural noun | _sarva_ |
| 24 | vayam | **mad** | nominative plural noun | _aj `accusative singular masculine noun`_ |
| 25 | atas | **atas** | — | _ad `nominative singular masculine noun`_ |
| 26 | param | **param** | — | _a `nominative singular masculine noun`_ |
| 27 | param | **—** | — | _pṝ `accusative singular masculine noun`_ |


## BG 2.41 — Krishna

**Devanāgarī:** व्यवसायात्मिका बुद्धिर् एकेह कुरु-नन्दन | बहु-शाखा ह्य् अनन्ताश् च बुद्धयो ऽव्यवसायिनाम्

**IAST:** *vyavasāyātmikā buddhir ekeha kuru-nandana | bahu-śākhā hy anantāś ca buddhayo 'vyavasāyinām*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | vyavasāya | **vyavasāya** | compound (compound member) | _—_ |
| 1 | ātmikā | **ātmaka** | nominative feminine singular noun | _budh_ |
| 2 | buddhiḥ | **buddhi** | nominative feminine singular noun | _ej `nominative singular masculine noun`_ |
| 3 | ekā | **eka** | nominative feminine singular noun | _a `vocative singular masculine noun`_ |
| 4 | iha | **iha** | — | _īh `vocative singular masculine noun`_ |
| 5 | kuru | **kuru** | compound (compound member) | _kṛ_ |
| 6 | nandana | **nandana** | vocative masculine singular noun | _—_ |
| 7 | bahu | **bahu** | compound (compound member) | _nandi_ |
| 8 | śākhāḥ | **śākhā** | nominative feminine plural noun | _bahu_ |
| 9 | hi | **hi** | — | _—_ |
| 10 | anantāḥ | **ananta** | nominative feminine plural noun | _śākhā_ |
| 11 | ca | **ca** | — | _hi `nominative singular masculine noun`_ |
| 12 | buddhayaḥ | **buddhi** | nominative feminine plural noun | _an `nominative singular masculine noun`_ |
| 13 | avyavasāyinām | **avyavasāyin** | genitive masculine plural noun | _tāsi_ |
| 14 | ca | **—** | — | _ca `vocative singular masculine noun`_ |
| 15 | buddhayas | **—** | — | _budh_ |
| 16 | avi | **—** | — | _o `locative singular masculine noun`_ |
| 17 | avas | **—** | — | _u `nominative singular masculine noun`_ |
| 18 | āyinām | **—** | — | _i `Vibhakti.Sasthi plural masculine noun`_ |


## BG 3.17 — Krishna

**Devanāgarī:** यस् त्व् आत्म-रतिर् एव स्याद् आत्म-तृप्तश् च मानवः | आत्मन्य् एव च संतुष्टस् तस्य कार्यं न विद्यते

**IAST:** *yas tv ātma-ratir eva syād ātma-tṛptaś ca mānavaḥ | ātmany eva ca saṃtuṣṭas tasya kāryaṃ na vidyate*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | yaḥ | **yad** | nominative masculine singular noun | _ī `nominative plural masculine noun`_ |
| 1 | tu | **tu** | — | _tu `nominative singular masculine noun`_ |
| 2 | ātma | **ātman** | compound (compound member) | _a `ablative singular masculine noun`_ |
| 3 | ratiḥ | **rati** | nominative masculine singular noun | _ma `vocative singular masculine noun`_ |
| 4 | eva | **eva** | — | _—_ |
| 5 | syāt | **as** | present optative 3rd person singular verb | _ram_ |
| 6 | ātma | **ātman** | compound (compound member) | _eva_ |
| 7 | tṛptaḥ | **tṛp** | nominative masculine singular participle noun | _as_ |
| 8 | ca | **ca** | — | _a `ablative singular masculine noun`_ |
| 9 | mānavaḥ | **mānava** | nominative masculine singular noun | _ma `vocative singular masculine noun`_ |
| 10 | ātmani | **ātman** | locative masculine singular noun | _—_ |
| 11 | eva | **eva** | — | _tṛp_ |
| 12 | ca | **ca** | — | _ca `vocative singular masculine noun`_ |
| 13 | saṃtuṣṭaḥ | **saṃtuṣ** | nominative masculine singular participle noun | _mānava_ |
| 14 | tasya | **tad** | genitive masculine singular noun | _a `ablative singular masculine noun`_ |
| 15 | kāryam | **kārya** | nominative neuter singular noun | _maṅki_ |
| 16 | na | **na** | — | _i `nominative singular masculine noun`_ |
| 17 | vidyate | **vid** | present indicative pass 3rd person singular verb | _eva_ |
| 18 | ca | **—** | — | _ca `vocative singular masculine noun`_ |
| 19 | saṃtuṣṭas | **—** | — | _saṃtuṣ_ |
| 20 | tasya | **—** | — | _tad_ |
| 21 | kāryam | **—** | — | _kṛ `accusative singular masculine noun`_ |
| 22 | na | **—** | — | _na `vocative singular neuter noun`_ |
| 23 | vidyate | **—** | — | _vid_ |


## BG 3.22 — Krishna

**Devanāgarī:** यद्य् अत्र ते लोक-संग्रह-कर्तव्यतायां विप्रतिपत्तिस् तर्हि मां किं न पश्यसि ? न मे पार्थास्ति कर्तव्यं त्रिषु लोकेषु किंचन | नानवाप्तम् अवाप्तव्यं वर्तैव च कर्मणि

**IAST:** *yady atra te loka-saṃgraha-kartavyatāyāṃ vipratipattis tarhi māṃ kiṃ na paśyasi ? na me pārthāsti kartavyaṃ triṣu lokeṣu kiṃcana | nānavāptam avāptavyaṃ vartaiva ca karmaṇi*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | yadi | **yadi** | — | _yadi_ |
| 1 | atra | **atra** | — | _atra_ |
| 2 | te | **tvad** | genitive singular noun | _tā `nominative dual feminine noun`_ |
| 3 | loka | **loka** | compound (compound member) | _lok_ |
| 4 | saṃgraha | **saṃgraha** | compound (compound member) | _—_ |
| 5 | kartavya | **kṛ** | compound gdv (compound member) | _saṃgrah_ |
| 6 | tāyām | **tā** | locative feminine singular noun | _—_ |
| 7 | vipratipattiḥ | **vipratipatti** | nominative feminine singular noun | _kartavyatā_ |
| 8 | tarhi | **tarhi** | — | _vipratipatti_ |
| 9 | mām | **mad** | accusative singular noun | _tarhi_ |
| 10 | kim | **kim** | — | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 11 | na | **na** | — | _kim_ |
| 12 | paśyasi | **dṛś** | present indicative 2nd person singular verb | _na `vocative singular neuter noun`_ |
| 13 | na | **na** | — | _dṛś_ |
| 14 | me | **mad** | genitive singular noun | _na `vocative singular neuter noun`_ |
| 15 | pārtha | **pārtha** | vocative masculine singular noun | _mā `locative singular neuter noun`_ |
| 16 | asti | **as** | present indicative 3rd person singular verb | _pārtha_ |
| 17 | kartavyam | **kṛ** | nominative neuter singular gdv noun | _as_ |
| 18 | triṣu | **tri** | locative masculine plural noun | _kṛ `accusative singular masculine noun`_ |
| 19 | lokeṣu | **loka** | locative masculine plural noun | _tri_ |
| 20 | kiṃcana | **kaścana** | nominative neuter singular noun | _lok_ |
| 21 | na | **na** | — | _i `locative plural masculine noun`_ |
| 22 | anavāptam | **anavāpta** | nominative neuter singular noun | _kim_ |
| 23 | avāptavyam | **avāp** | nominative neuter singular gdv noun | _can_ |
| 24 | vartā | **vṛt** | future indicative peri 3rd person singular verb | _na `accusative plural masculine noun`_ |
| 25 | eva | **eva** | — | _vap_ |
| 26 | ca | **ca** | — | _u `vocative singular masculine noun`_ |
| 27 | karmaṇi | **karman** | locative neuter singular noun | _āp `accusative singular masculine noun`_ |
| 28 | vartā | **—** | — | _vṛ_ |
| 29 | eva | **—** | — | _eva_ |
| 30 | ca | **—** | — | _ca `vocative singular masculine noun`_ |
| 31 | karmaṇi | **—** | — | _karman_ |


## BG 3.23 — Krishna

**Devanāgarī:** यदि ह्य् अहं न वर्तेयं जातु कर्मण्य् अतन्द्रितः | मम वर्त्मानुवर्तन्ते मनुष्याः पार्थ सर्वशः

**IAST:** *yadi hy ahaṃ na varteyaṃ jātu karmaṇy atandritaḥ | mama vartmānuvartante manuṣyāḥ pārtha sarvaśaḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | yadi | **yadi** | — | _yadi_ |
| 1 | hi | **hi** | — | _hi `nominative singular masculine noun`_ |
| 2 | aham | **mad** | nominative singular noun | _aha_ |
| 3 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 4 | varteyam | **vṛt** | present optative 1st person singular verb | _vṛt_ |
| 5 | jātu | **jātu** | — | _jātu_ |
| 6 | karmaṇi | **karman** | locative neuter singular noun | _karman_ |
| 7 | atandritaḥ | **atandrita** | nominative masculine singular noun | _atandrita_ |
| 8 | mama | **mad** | genitive singular noun | _mā_ |
| 9 | vartma | **vartman** | accusative neuter singular noun | _vartman_ |
| 10 | anuvartante | **anuvṛt** | present indicative 3rd person plural verb | _a `nominative plural masculine noun`_ |
| 11 | manuṣyāḥ | **manuṣya** | nominative masculine plural noun | _nū_ |
| 12 | pārtha | **pārtha** | vocative masculine singular noun | _ṛ `nominative singular masculine noun`_ |
| 13 | sarvaśas | **sarvaśas** | — | _anti_ |
| 14 | manuṣi | **—** | — | _manus_ |
| 15 | ās | **—** | — | _a `nominative plural masculine noun`_ |
| 16 | pārtha | **—** | — | _pārtha_ |
| 17 | sarvaśas | **—** | — | _sarvaśas_ |


## BG 4.14 — Krishna

**Devanāgarī:** न मां कर्माणि लिम्पन्ति न मे कर्म-फले स्पृहा | इति मां यो ऽभिजानाति कर्मभिर् न स बध्यते

**IAST:** *na māṃ karmāṇi limpanti na me karma-phale spṛhā | iti māṃ yo 'bhijānāti karmabhir na sa badhyate*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 1 | mām | **mad** | accusative singular noun | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 2 | karmāṇi | **karman** | nominative neuter plural noun | _karman_ |
| 3 | limpanti | **lip** | present indicative 3rd person plural verb | _lip_ |
| 4 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 5 | me | **mad** | genitive singular noun | _mā `locative singular neuter noun`_ |
| 6 | karma | **karman** | compound (compound member) | _karman_ |
| 7 | phale | **phala** | locative neuter singular noun | _—_ |
| 8 | spṛhā | **spṛhā** | nominative feminine singular noun | _phal_ |
| 9 | iti | **iti** | — | _spṛhā_ |
| 10 | mām | **mad** | accusative singular noun | _i `nominative singular neuter noun`_ |
| 11 | yaḥ | **yad** | nominative masculine singular noun | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 12 | abhijānāti | **abhijñā** | present indicative 3rd person singular verb | _ī `nominative plural masculine noun`_ |
| 13 | karmabhiḥ | **karman** | instrumental neuter plural noun | _abhijñā_ |
| 14 | na | **na** | — | _karman_ |
| 15 | sa | **tad** | nominative masculine singular noun | _na `vocative singular neuter noun`_ |
| 16 | badhyate | **bandh** | present indicative pass 3rd person singular verb | _sa `vocative singular masculine noun`_ |
| 17 | badhyate | **—** | — | _bandh_ |


## BG 4.15 — Krishna

**Devanāgarī:** एवं ज्ञात्वा कृतं कर्म पूर्वैर् अपि मुमुक्षुभिः | कुरु कर्मैव तस्मात् त्वं पूर्वैः पूर्वतरं कृतम्

**IAST:** *evaṃ jñātvā kṛtaṃ karma pūrvair api mumukṣubhiḥ | kuru karmaiva tasmāt tvaṃ pūrvaiḥ pūrvataraṃ kṛtam*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | evam | **evam** | — | _eva_ |
| 1 | jñātvā | **jñā** | conv | _jñā_ |
| 2 | kṛtam | **kṛ** | accusative neuter singular participle noun | _kṛ `accusative singular masculine noun`_ |
| 3 | karma | **karman** | accusative neuter singular noun | _karman_ |
| 4 | pūrvaiḥ | **pūrva** | instrumental masculine plural noun | _pūrva_ |
| 5 | api | **api** | — | _api_ |
| 6 | mumukṣubhiḥ | **mumukṣu** | instrumental masculine plural noun | _mumukṣu_ |
| 7 | kuru | **kṛ** | present imperative 2nd person singular verb | _kṛ_ |
| 8 | karma | **karman** | accusative neuter singular noun | _karman_ |
| 9 | eva | **eva** | — | _eva_ |
| 10 | tasmāt | **tasmāt** | — | _tasmāt_ |
| 11 | tvam | **tvad** | nominative singular noun | _tva_ |
| 12 | pūrvaiḥ | **pūrva** | instrumental masculine plural noun | _pūrva_ |
| 13 | pūrvataram | **pūrvatara** | accusative neuter singular noun | _pūru_ |
| 14 | kṛtam | **kṛ** | accusative neuter singular participle noun | _tṝ_ |
| 15 | kṛtam | **—** | — | _kṛ `accusative singular masculine noun`_ |


## BG 4.40 — Krishna

**Devanāgarī:** अज्ञश् चाश्रद्दधानश् च संशयात्मा विनश्यति | नायं लोको ऽस्ति न परो न सुखं संशयात्मनः

**IAST:** *ajñaś cāśraddadhānaś ca saṃśayātmā vinaśyati | nāyaṃ loko 'sti na paro na sukhaṃ saṃśayātmanaḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | ajñaḥ | **ajña** | nominative masculine singular noun | _ajña_ |
| 1 | ca | **ca** | — | _ca `vocative singular masculine noun`_ |
| 2 | aśraddadhānaḥ | **aśraddadhāna** | nominative masculine singular noun | _aśraddadhāna_ |
| 3 | ca | **ca** | — | _ca `vocative singular masculine noun`_ |
| 4 | saṃśaya | **saṃśaya** | compound (compound member) | _saṃśī_ |
| 5 | ātmā | **ātman** | nominative masculine singular noun | _mā `vocative singular neuter noun`_ |
| 6 | vinaśyati | **vinaś** | present indicative 3rd person singular verb | _vinaś_ |
| 7 | na | **na** | — | _nī `accusative singular masculine noun`_ |
| 8 | ayam | **idam** | nominative masculine singular noun | _la `vocative singular masculine noun`_ |
| 9 | lokaḥ | **loka** | nominative masculine singular noun | _vac_ |
| 10 | asti | **as** | present indicative 3rd person singular verb | _a `nominative singular masculine noun`_ |
| 11 | na | **na** | — | _as_ |
| 12 | paraḥ | **para** | nominative masculine singular noun | _na `vocative singular neuter noun`_ |
| 13 | na | **na** | — | _pṝ `nominative singular masculine noun`_ |
| 14 | sukham | **sukha** | nominative neuter singular noun | _na `vocative singular neuter noun`_ |
| 15 | saṃśaya | **saṃśaya** | compound (compound member) | _sukham_ |
| 16 | ātmanaḥ | **ātman** | genitive masculine singular noun | _saṃśī_ |
| 17 | manas | **—** | — | _man_ |


## BG 5.10 — Krishna

**Devanāgarī:** ब्रह्मण्य् आधाय कर्माणि सङ्गं त्यक्त्वा करोति यः | लिप्यते न स पापेन पद्म-पत्रम् इवाम्भसा

**IAST:** *brahmaṇy ādhāya karmāṇi saṅgaṃ tyaktvā karoti yaḥ | lipyate na sa pāpena padma-patram ivāmbhasā*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | brahmaṇi | **brahman** | locative neuter singular noun | _brahman_ |
| 1 | ādhāya | **ādhā** | conv | _ādhā_ |
| 2 | karmāṇi | **karman** | accusative neuter plural noun | _karman_ |
| 3 | saṅgam | **saṅga** | accusative masculine singular noun | _sañj_ |
| 4 | tyaktvā | **tyaj** | conv | _tyaj_ |
| 5 | karoti | **kṛ** | present indicative 3rd person singular verb | _kṛ_ |
| 6 | yaḥ | **yad** | nominative masculine singular noun | _ī `nominative plural masculine noun`_ |
| 7 | lipyate | **lip** | present indicative pass 3rd person singular verb | _lip_ |
| 8 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 9 | sa | **tad** | nominative masculine singular noun | _sa `vocative singular masculine noun`_ |
| 10 | pāpena | **pāpa** | instrumental neuter singular noun | _pāpa_ |
| 11 | padma | **padma** | compound (compound member) | _padma_ |
| 12 | patram | **pattra** | nominative neuter singular noun | _—_ |
| 13 | iva | **iva** | — | _pat_ |
| 14 | ambhasā | **ambhas** | instrumental neuter singular noun | _ra `accusative singular masculine noun`_ |
| 15 | iva | **—** | — | _iva_ |
| 16 | ambhasā | **—** | — | _ambhas_ |


## BG 5.21 — Krishna

**Devanāgarī:** बाह्य-स्पर्शेष्व् असक्तात्मा विन्दत्य् आत्मनि यत् सुखम् | स ब्रह्म-योग-युक्तात्मा सुखम् अक्षयम् अश्नुते

**IAST:** *bāhya-sparśeṣv asaktātmā vindaty ātmani yat sukham | sa brahma-yoga-yuktātmā sukham akṣayam aśnute*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | bāhya | **bāhya** | compound (compound member) | _bāhi_ |
| 1 | sparśeṣu | **sparśa** | locative masculine plural noun | _—_ |
| 2 | asakta | **asakta** | compound (compound member) | _spṛś_ |
| 3 | ātmā | **ātman** | nominative masculine singular noun | _a `nominative singular masculine noun`_ |
| 4 | vindati | **vid** | present indicative 3rd person singular verb | _añj_ |
| 5 | ātmani | **ātman** | locative masculine singular noun | _mā `vocative singular neuter noun`_ |
| 6 | yat | **yad** | accusative neuter singular noun | _vid_ |
| 7 | sukham | **sukha** | accusative neuter singular noun | _a `ablative singular masculine noun`_ |
| 8 | sa | **tad** | nominative masculine singular noun | _maṅki_ |
| 9 | brahma | **brahman** | compound (compound member) | _i `nominative singular masculine noun`_ |
| 10 | yoga | **yoga** | compound (compound member) | _yat_ |
| 11 | yukta | **yuj** | compound participle (compound member) | _sukham_ |
| 12 | ātmā | **ātman** | nominative masculine singular noun | _sa `nominative singular masculine noun`_ |
| 13 | sukham | **sukha** | accusative neuter singular noun | _brahman_ |
| 14 | akṣayam | **akṣaya** | accusative neuter singular noun | _—_ |
| 15 | aśnute | **aś** | present indicative 3rd person singular verb | _yuj_ |
| 16 | - | **—** | — | _—_ |
| 17 | yuktāt | **—** | — | _yuj_ |
| 18 | mā | **—** | — | _mā `vocative singular neuter noun`_ |
| 19 | sukham | **—** | — | _sukham_ |
| 20 | akṣayam | **—** | — | _kṣi_ |
| 21 | aśnute | **—** | — | _aś_ |


## BG 5.26 — Krishna

**Devanāgarī:** काम-क्रोध-वियुक्तानां यतीनां यत-चेतसाम् | अभितो ब्रह्म-निर्वाणं वर्तते विदितात्मनाम्

**IAST:** *kāma-krodha-viyuktānāṃ yatīnāṃ yata-cetasām | abhito brahma-nirvāṇaṃ vartate viditātmanām*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | kāma | **kāma** | compound (compound member) | _kāma_ |
| 1 | krodha | **krodha** | compound (compound member) | _—_ |
| 2 | viyuktānām | **viyuj** | genitive masculine plural participle noun | _krodha_ |
| 3 | yatīnām | **yati** | genitive masculine plural noun | _—_ |
| 4 | yata | **yam** | compound participle (compound member) | _viyuj_ |
| 5 | cetasām | **cetas** | genitive masculine plural noun | _yam_ |
| 6 | abhitas | **abhitas** | — | _yat_ |
| 7 | brahma | **brahman** | compound (compound member) | _—_ |
| 8 | nirvāṇam | **nirvāṇa** | nominative neuter singular noun | _cit_ |
| 9 | vartate | **vṛt** | present indicative 3rd person singular verb | _ā `accusative singular masculine noun`_ |
| 10 | vidita | **vid** | compound participle (compound member) | _abhitas_ |
| 11 | ātmanām | **ātman** | genitive masculine plural noun | _brahman_ |
| 12 | - | **—** | — | _—_ |
| 13 | nis | **—** | — | _ni `nominative singular masculine noun`_ |
| 14 | vās | **—** | — | _vā `nominative singular masculine noun`_ |
| 15 | ṇam | **—** | — | _ṇa `accusative singular masculine noun`_ |
| 16 | vartate | **—** | — | _vṛt_ |
| 17 | viditāt | **—** | — | _vid_ |
| 18 | manām | **—** | — | _man_ |


## BG 6.10 — Krishna

**Devanāgarī:** योगी युञ्जीत सततम् आत्मानं रहसि स्थितः | एकाकी यत-चित्तात्मा निराशीर् अपरिग्रहः

**IAST:** *yogī yuñjīta satatam ātmānaṃ rahasi sthitaḥ | ekākī yata-cittātmā nirāśīr aparigrahaḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | yogī | **yogin** | nominative masculine singular noun | _yogin_ |
| 1 | yuñjīta | **yuj** | present optative 3rd person singular verb | _yuj_ |
| 2 | satatam | **satatam** | — | _satata_ |
| 3 | ātmānam | **ātman** | accusative masculine singular noun | _a `ablative singular masculine noun`_ |
| 4 | rahasi | **rahas** | locative neuter singular noun | _mā `accusative singular masculine noun`_ |
| 5 | sthitaḥ | **sthā** | nominative masculine singular participle noun | _rah_ |
| 6 | ekākī | **ekākin** | nominative masculine singular noun | _sthā_ |
| 7 | yata | **yam** | compound participle (compound member) | _ekākin_ |
| 8 | citta | **citta** | compound (compound member) | _yat_ |
| 9 | ātmā | **ātman** | nominative masculine singular noun | _—_ |
| 10 | nirāśīḥ | **nirāśī** | nominative masculine singular noun | _cit_ |
| 11 | aparigrahaḥ | **aparigraha** | nominative masculine singular noun | _mā `vocative singular neuter noun`_ |
| 12 | nirāśīs | **—** | — | _niraś_ |
| 13 | aparigrahas | **—** | — | _aparigraha_ |


## BG 6.14 — Krishna

**Devanāgarī:** प्रशान्तात्मा विगत-भीर् ब्रह्मचारि-व्रते स्थितः | मनः संयम्य मच्-चित्तो युक्त आसीत मत्-परः

**IAST:** *praśāntātmā vigata-bhīr brahmacāri-vrate sthitaḥ | manaḥ saṃyamya mac-citto yukta āsīta mat-paraḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | praśānta | **praśam** | compound participle (compound member) | _—_ |
| 1 | ātmā | **ātman** | nominative masculine singular noun | _—_ |
| 2 | vigata | **vigam** | compound participle (compound member) | _—_ |
| 3 | bhīḥ | **bhī** | nominative masculine singular noun | _—_ |
| 4 | brahmacāri | **brahmacārin** | compound (compound member) | _—_ |
| 5 | vrate | **vrata** | locative neuter singular noun | _—_ |
| 6 | sthitaḥ | **sthā** | nominative masculine singular participle noun | _—_ |
| 7 | manaḥ | **manas** | accusative neuter singular noun | _—_ |
| 8 | saṃyamya | **saṃyam** | conv | _—_ |
| 9 | mad | **mad** | compound (compound member) | _—_ |
| 10 | cittaḥ | **citta** | nominative masculine singular noun | _—_ |
| 11 | yuktaḥ | **yuj** | nominative masculine singular participle noun | _—_ |
| 12 | āsīta | **ās** | present optative 3rd person singular verb | _—_ |
| 13 | mad | **mad** | compound (compound member) | _—_ |
| 14 | paraḥ | **para** | nominative masculine singular noun | _—_ |


## BG 6.21 — Krishna

**Devanāgarī:** सुखम् आत्यन्तिकं यत् तद् बुद्धि-ग्राह्यम् अतीन्द्रियम् | वेत्ति यत्र न चैवायं स्थितश् चलति तत्त्वतः

**IAST:** *sukham ātyantikaṃ yat tad buddhi-grāhyam atīndriyam | vetti yatra na caivāyaṃ sthitaś calati tattvataḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | sukham | **sukha** | nominative neuter singular noun | _sukham_ |
| 1 | ātyantikam | **ātyantika** | nominative neuter singular noun | _ātyantika_ |
| 2 | yat | **yad** | nominative neuter singular noun | _yat_ |
| 3 | tat | **tad** | accusative neuter singular noun | _tad_ |
| 4 | buddhi | **buddhi** | compound (compound member) | _budh_ |
| 5 | grāhyam | **grah** | accusative neuter singular gdv noun | _—_ |
| 6 | atīndriyam | **atīndriya** | accusative neuter singular noun | _grah_ |
| 7 | vetti | **vid** | present indicative 3rd person singular verb | _ati_ |
| 8 | yatra | **yatra** | — | _indriya_ |
| 9 | na | **na** | — | _vid_ |
| 10 | ca | **ca** | — | _yatra_ |
| 11 | eva | **eva** | — | _na `vocative singular neuter noun`_ |
| 12 | ayam | **idam** | nominative masculine singular noun | _ca `vocative singular masculine noun`_ |
| 13 | sthitaḥ | **sthā** | nominative masculine singular participle noun | _eva_ |
| 14 | calati | **cal** | present indicative 3rd person singular verb | _i `accusative singular masculine noun`_ |
| 15 | tattvataḥ | **tattva** | ablative neuter singular noun | _sthā_ |
| 16 | calati | **—** | — | _cal_ |
| 17 | tat | **—** | — | _tad_ |
| 18 | tu | **—** | — | _tu `nominative singular masculine noun`_ |
| 19 | at | **—** | — | _ad `nominative singular masculine noun`_ |
| 20 | as | **—** | — | _a `nominative singular masculine noun`_ |


## BG 7.16 — Krishna

**Devanāgarī:** चतुर्-विधा भजन्ते मां जनाः सुकृतिनो ऽर्जुन | आर्तो जिज्ञासुर् अर्थार्थी ज्ञानी च भरतर्षभ

**IAST:** *catur-vidhā bhajante māṃ janāḥ sukṛtino 'rjuna | ārto jijñāsur arthārthī jñānī ca bharatarṣabha*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | catur | **catur** | compound (compound member) | _—_ |
| 1 | vidhāḥ | **vidha** | nominative masculine plural noun | _—_ |
| 2 | bhajante | **bhaj** | present indicative 3rd person plural verb | _vidhā_ |
| 3 | mām | **mad** | accusative singular noun | _bhaj_ |
| 4 | janāḥ | **jana** | nominative masculine plural noun | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 5 | sukṛtinaḥ | **sukṛtin** | nominative masculine plural noun | _jana_ |
| 6 | arjuna | **arjuna** | vocative masculine singular noun | _sukṛt_ |
| 7 | ārtaḥ | **ārta** | nominative masculine singular noun | _indh_ |
| 8 | jijñāsuḥ | **jijñāsu** | nominative masculine singular noun | _a `nominative singular masculine noun`_ |
| 9 | artha | **artha** | compound (compound member) | _arjuna_ |
| 10 | arthī | **arthin** | nominative masculine singular noun | _ārta_ |
| 11 | jñānī | **jñānin** | nominative masculine singular noun | _jijñāsa_ |
| 12 | ca | **ca** | — | _arthārthin_ |
| 13 | bharata | **bharata** | compound (compound member) | _jñā_ |
| 14 | ṛṣabha | **ṛṣabha** | vocative masculine singular noun | _ca `vocative singular masculine noun`_ |
| 15 | bharatarṣabha | **—** | — | _bharataṛṣabha_ |


## BG 7.24 — Krishna

**Devanāgarī:** अव्यक्तं व्यक्तिम् आपन्नं मन्यन्ते माम् अबुद्धयः | परं भावम् अजानन्तो ममाव्ययम् अनुत्तमम्

**IAST:** *avyaktaṃ vyaktim āpannaṃ manyante mām abuddhayaḥ | paraṃ bhāvam ajānanto mamāvyayam anuttamam*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | avyaktam | **avyakta** | accusative neuter singular noun | _avyakta_ |
| 1 | vyaktim | **vyakti** | accusative feminine singular noun | _vyañj_ |
| 2 | āpannam | **āpad** | accusative masculine singular participle noun | _āpad_ |
| 3 | manyante | **man** | present indicative 3rd person plural verb | _man_ |
| 4 | mām | **mad** | accusative singular noun | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 5 | abuddhayaḥ | **abuddhi** | nominative masculine plural noun | _abuddhi_ |
| 6 | param | **para** | accusative masculine singular noun | _pṝ `accusative singular masculine noun`_ |
| 7 | bhāvam | **bhāva** | accusative masculine singular noun | _bhū_ |
| 8 | a | **a** | — | _aj `instrumental singular masculine noun`_ |
| 9 | jānantaḥ | **jñā** | nominative masculine plural present participle verb | _an `nominative plural masculine noun`_ |
| 10 | mama | **mad** | genitive singular noun | _mā_ |
| 11 | avyayam | **avyaya** | accusative masculine singular noun | _āvye_ |
| 12 | anuttamam | **anuttama** | accusative masculine singular noun | _añji_ |
| 13 | uttamam | **—** | — | _uttama_ |


## BG 7.27 — Krishna

**Devanāgarī:** इच्छा-द्वेष-समुत्थेन द्वन्द्व-मोहेन भारत | सर्व-भूतानि संमोहं सर्गे यान्ति परन्तप

**IAST:** *icchā-dveṣa-samutthena dvandva-mohena bhārata | sarva-bhūtāni saṃmohaṃ sarge yānti parantapa*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | icchā | **icchā** | compound (compound member) | _iṣ `instrumental singular masculine noun`_ |
| 1 | dveṣa | **dveṣa** | compound (compound member) | _—_ |
| 2 | samutthena | **samuttha** | instrumental masculine singular noun | _dviṣ_ |
| 3 | dvandva | **dvaṃdva** | compound (compound member) | _—_ |
| 4 | mohena | **moha** | instrumental masculine singular noun | _samutthā_ |
| 5 | bhārata | **bhārata** | vocative masculine singular noun | _dvaṃdva_ |
| 6 | sarva | **sarva** | compound (compound member) | _—_ |
| 7 | bhūtāni | **bhūta** | nominative neuter plural noun | _muh_ |
| 8 | saṃmoham | **sammoha** | accusative masculine singular noun | _bhū_ |
| 9 | sarge | **sarga** | locative masculine singular noun | _ram_ |
| 10 | yānti | **yā** | present indicative 3rd person plural verb | _sarva_ |
| 11 | parantapa | **paraṃtapa** | vocative masculine singular noun | _—_ |
| 12 | bhūtāni | **—** | — | _bhū_ |
| 13 | sam | **—** | — | _sa `accusative singular masculine noun`_ |
| 14 | moham | **—** | — | _muh_ |
| 15 | sarge | **—** | — | _sṛj_ |
| 16 | yānti | **—** | — | _yā_ |
| 17 | parantapa | **—** | — | _paraṃtapa_ |


## BG 8.1 — Krishna

**Devanāgarī:** किं तद् ब्रह्म किम् अध्यात्मं किं कर्म पुरुषोत्तम | अधिभूतं च किं प्रोक्तम् अधिदैवं किम् उच्यते

**IAST:** *kiṃ tad brahma kim adhyātmaṃ kiṃ karma puruṣottama | adhibhūtaṃ ca kiṃ proktam adhidaivaṃ kim ucyate*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | kim | **ka** | nominative neuter singular noun | _kim_ |
| 1 | tat | **tad** | nominative neuter singular noun | _tad_ |
| 2 | brahma | **brahman** | nominative neuter singular noun | _brahman_ |
| 3 | kim | **ka** | nominative neuter singular noun | _kim_ |
| 4 | adhyātmam | **adhyātma** | nominative neuter singular noun | _adhyātmam_ |
| 5 | kim | **ka** | nominative neuter singular noun | _kim_ |
| 6 | karma | **karman** | nominative neuter singular noun | _karman_ |
| 7 | puruṣottama | **puruṣottama** | vocative masculine singular noun | _puruṣottama_ |
| 8 | adhibhūtam | **adhibhūta** | nominative neuter singular noun | _adhibhūta_ |
| 9 | ca | **ca** | — | _ca `vocative singular masculine noun`_ |
| 10 | kim | **ka** | nominative neuter singular noun | _kim_ |
| 11 | proktam | **pravac** | nominative neuter singular participle noun | _pravac_ |
| 12 | adhidaivam | **adhidaiva** | nominative neuter singular noun | _adhidaivam_ |
| 13 | kim | **ka** | nominative neuter singular noun | _kim_ |
| 14 | ucyate | **vac** | present indicative pass 3rd person singular verb | _vac_ |


## BG 8.15 — Krishna

**Devanāgarī:** माम् उपेत्य पुनर्-जन्म दुःखालयम् अशाश्वतम् | नाप्नुवन्ति महात्मानः संसिद्धिं परमां गताः

**IAST:** *mām upetya punar-janma duḥkhālayam aśāśvatam | nāpnuvanti mahātmānaḥ saṃsiddhiṃ paramāṃ gatāḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | mām | **mad** | accusative singular noun | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 1 | upetya | **upe** | conv | _vap_ |
| 2 | punar | **punar** | — | _i `vocative singular masculine noun`_ |
| 3 | janma | **janman** | accusative neuter singular noun | _punar_ |
| 4 | duḥkha | **duḥkha** | compound (compound member) | _—_ |
| 5 | ālayam | **ālaya** | accusative neuter singular noun | _janman_ |
| 6 | aśāśvatam | **aśāśvata** | accusative neuter singular noun | _dus_ |
| 7 | na | **na** | — | _khan_ |
| 8 | āpnuvanti | **āp** | present indicative 3rd person plural verb | _ālaya_ |
| 9 | mahātmānaḥ | **mahātman** | nominative masculine plural noun | _aśāśvata_ |
| 10 | saṃsiddhim | **saṃsiddhi** | accusative feminine singular noun | _na `vocative singular neuter noun`_ |
| 11 | paramām | **parama** | accusative feminine singular noun | _āp `nominative plural neuter noun`_ |
| 12 | gatāḥ | **gam** | nominative masculine plural participle noun | _mah_ |
| 13 | mānas | **—** | — | _mā `nominative singular masculine noun`_ |
| 14 | saṃsiddhim | **—** | — | _saṃsiddhi_ |
| 15 | paramām | **—** | — | _parama_ |
| 16 | gatās | **—** | — | _gam_ |


## BG 8.25 — Krishna

**Devanāgarī:** धूमो रात्रिस् तथा कृष्णः षण्-मासा दक्षिणायनम् | तत्र चान्द्रमसं ज्योतिर् योगी प्राप्य निवर्तते

**IAST:** *dhūmo rātris tathā kṛṣṇaḥ ṣaṇ-māsā dakṣiṇāyanam | tatra cāndramasaṃ jyotir yogī prāpya nivartate*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | dhūmaḥ | **dhūma** | nominative masculine singular noun | _dhū_ |
| 1 | rātriḥ | **rātri** | nominative feminine singular noun | _a `nominative singular masculine noun`_ |
| 2 | tathā | **tathā** | — | _rā `nominative singular neuter noun`_ |
| 3 | kṛṣṇaḥ | **kṛṣṇa** | nominative masculine singular noun | _i `nominative singular masculine noun`_ |
| 4 | ṣaṭ | **ṣaṣ** | nominative masculine plural noun | _tathā_ |
| 5 | māsāḥ | **māsa** | nominative masculine plural noun | _kṛṣṇa_ |
| 6 | dakṣiṇāyanam | **dakṣiṇāyana** | nominative neuter singular noun | _—_ |
| 7 | tatra | **tatra** | — | _—_ |
| 8 | cāndramasam | **cāndramasa** | accusative neuter singular noun | _māsa_ |
| 9 | jyotiḥ | **jyotis** | accusative neuter singular noun | _dakṣiṇā_ |
| 10 | yogī | **yogin** | nominative masculine singular noun | _i `accusative singular masculine noun`_ |
| 11 | prāpya | **prāp** | conv | _tad_ |
| 12 | nivartate | **nivṛt** | present indicative 3rd person singular verb | _ra `vocative singular neuter noun`_ |
| 13 | cāndramasam | **—** | — | _cāndramasa_ |
| 14 | jyotis | **—** | — | _jyotis_ |
| 15 | yogī | **—** | — | _yogin_ |
| 16 | pra | **—** | — | _pra_ |
| 17 | apya | **—** | — | _apya_ |
| 18 | nivartate | **—** | — | _nivṛt_ |


## BG 9.4 — Krishna

**Devanāgarī:** मया ततम् इदं सर्वं जगद् अव्यक्त-मूर्तिना | मत्-स्थानि सर्व-भूतानि न चाहं तेष्व् अवस्थितः

**IAST:** *mayā tatam idaṃ sarvaṃ jagad avyakta-mūrtinā | mat-sthāni sarva-bhūtāni na cāhaṃ teṣv avasthitaḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | mayā | **mad** | instrumental singular noun | _mā `instrumental singular feminine noun`_ |
| 1 | tatam | **tan** | nominative neuter singular participle noun | _tan_ |
| 2 | idam | **idam** | nominative neuter singular noun | _idam_ |
| 3 | sarvam | **sarva** | nominative neuter singular noun | _sarva_ |
| 4 | jagat | **jagant** | nominative neuter singular noun | _jagat_ |
| 5 | avyakta | **avyakta** | compound (compound member) | _avyakta_ |
| 6 | mūrtinā | **mūrti** | instrumental masculine singular noun | _—_ |
| 7 | mad | **mad** | compound (compound member) | _mūrch_ |
| 8 | sthāni | **stha** | nominative neuter plural noun | _math_ |
| 9 | sarva | **sarva** | compound (compound member) | _—_ |
| 10 | bhūtāni | **bhūta** | nominative neuter plural noun | _sthā_ |
| 11 | na | **na** | — | _sarva_ |
| 12 | ca | **ca** | — | _—_ |
| 13 | aham | **mad** | nominative singular noun | _bhū_ |
| 14 | teṣu | **tad** | locative neuter plural noun | _na `vocative singular neuter noun`_ |
| 15 | avasthitaḥ | **avasthā** | nominative masculine singular participle noun | _ca `nominative plural masculine noun`_ |
| 16 | ham | **—** | — | _ha `accusative singular masculine noun`_ |
| 17 | teṣu | **—** | — | _tad_ |
| 18 | avasthitas | **—** | — | _avasthā_ |


## BG 9.22 — Krishna

**Devanāgarī:** अनन्याश् चिन्तयन्तो मां ये जनाः पर्युपासते | तेषां नित्याभियुक्तानां योग-क्षेमं वहाम्य् अहम्

**IAST:** *ananyāś cintayanto māṃ ye janāḥ paryupāsate | teṣāṃ nityābhiyuktānāṃ yoga-kṣemaṃ vahāmy aham*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | an | **an** | — | _an `ablative singular feminine noun`_ |
| 1 | anyāḥ | **anya** | nominative masculine plural noun | _cint_ |
| 2 | cintayantaḥ | **cintay** | nominative masculine plural present participle verb | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 3 | mām | **mad** | accusative singular noun | _yā `locative singular neuter noun`_ |
| 4 | ye | **yad** | nominative masculine plural noun | _jana_ |
| 5 | janāḥ | **jana** | nominative masculine plural noun | _pari_ |
| 6 | paryupāsate | **paryupās** | present indicative 3rd person plural verb | _vap_ |
| 7 | teṣām | **tad** | genitive masculine plural noun | _as_ |
| 8 | nitya | **nitya** | compound (compound member) | _tad_ |
| 9 | abhiyuktānām | **abhiyuj** | genitive masculine plural participle noun | _nitya_ |
| 10 | yoga | **yoga** | compound (compound member) | _abhiyuj_ |
| 11 | kṣemam | **kṣema** | accusative neuter singular noun | _yuj_ |
| 12 | vahāmi | **vah** | present indicative 1st person singular verb | _—_ |
| 13 | aham | **mad** | nominative singular noun | _kṣā_ |
| 14 | im | **—** | — | _i `accusative singular masculine noun`_ |
| 15 | am | **—** | — | _a `accusative singular masculine noun`_ |
| 16 | vahāmi | **—** | — | _vah_ |
| 17 | aham | **—** | — | _aha_ |


## BG 9.33 — Krishna

**Devanāgarī:** किं पुनर् ब्राह्मणाः पुण्या भक्ता राजर्षयस् तथा | अनित्यम् असुखं लोकम् इमं प्राप्य भजस्व माम्

**IAST:** *kiṃ punar brāhmaṇāḥ puṇyā bhaktā rājarṣayas tathā | anityam asukhaṃ lokam imaṃ prāpya bhajasva mām*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | kim | **ka** | nominative neuter singular noun | _kim_ |
| 1 | punar | **punar** | — | _punar_ |
| 2 | brāhmaṇāḥ | **brāhmaṇa** | nominative masculine plural noun | _brāhmaṇa_ |
| 3 | puṇyāḥ | **puṇya** | nominative masculine plural noun | _puṇya_ |
| 4 | bhaktāḥ | **bhakta** | nominative masculine plural noun | _bhaj_ |
| 5 | rājarṣayaḥ | **rājarṣi** | nominative masculine plural noun | _rājarṣi_ |
| 6 | tathā | **tathā** | — | _tathā_ |
| 7 | anityam | **anitya** | accusative masculine singular noun | _anitya_ |
| 8 | asukham | **asukha** | accusative masculine singular noun | _asukha_ |
| 9 | lokam | **loka** | accusative masculine singular noun | _la `vocative singular masculine noun`_ |
| 10 | imam | **idam** | accusative masculine singular noun | _vac_ |
| 11 | prāpya | **prāp** | conv | _a `accusative singular masculine noun`_ |
| 12 | bhajasva | **bhaj** | present imperative 2nd person singular verb | _i `accusative singular masculine noun`_ |
| 13 | mām | **mad** | accusative singular noun | _a `accusative singular masculine noun`_ |
| 14 | pra | **—** | — | _pra_ |
| 15 | apya | **—** | — | _apya_ |
| 16 | bhajasva | **—** | — | _bhaj_ |
| 17 | mām | **—** | — | _mā `Vibhakti.Sasthi plural neuter noun`_ |


## BG 10.1 — Krishna

**Devanāgarī:** भूय एव महा-बाहो शृणु मे परमं वचः | यत् ते ऽहं प्रीयमाणाय वक्ष्यामि हित-काम्यया

**IAST:** *bhūya eva mahā-bāho śṛṇu me paramaṃ vacaḥ | yat te 'haṃ prīyamāṇāya vakṣyāmi hita-kāmyayā*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | bhūyas | **bhūyas** | — | _bhūyas_ |
| 1 | eva | **eva** | — | _eva_ |
| 2 | mahā | **mahat** | compound (compound member) | _mah_ |
| 3 | bāho | **bāhu** | vocative masculine singular noun | _—_ |
| 4 | śṛṇu | **śru** | present imperative 2nd person singular verb | _bāhu_ |
| 5 | me | **mad** | genitive singular noun | _śru_ |
| 6 | paramam | **parama** | accusative neuter singular noun | _mā `locative singular neuter noun`_ |
| 7 | vacaḥ | **vacas** | accusative neuter singular noun | _parama_ |
| 8 | yat | **yad** | accusative neuter singular noun | _vac_ |
| 9 | te | **tvad** | dative singular noun | _yat_ |
| 10 | aham | **mad** | nominative singular noun | _tā `nominative dual feminine noun`_ |
| 11 | prīyamāṇāya | **prī** | dative masculine singular present participle pass verb | _aha_ |
| 12 | vakṣyāmi | **vac** | future indicative 1st person singular verb | _prī_ |
| 13 | hita | **hita** | compound (compound member) | _vac_ |
| 14 | kāmyayā | **kāmyā** | instrumental feminine singular noun | _hi `vocative singular masculine noun`_ |
| 15 | - | **—** | — | _—_ |
| 16 | kāmyayā | **—** | — | _kāmyā_ |


## BG 10.5 — Krishna

**Devanāgarī:** अहिंसा समता तुष्टिस् तपो दानं यशो ऽयशः | भवन्ति भावा भूतानां मत्त एव पृथग्-विधाः

**IAST:** *ahiṃsā samatā tuṣṭis tapo dānaṃ yaśo 'yaśaḥ | bhavanti bhāvā bhūtānāṃ matta eva pṛthag-vidhāḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | ahiṃsā | **ahiṃsā** | nominative feminine singular noun | _—_ |
| 1 | sama | **sama** | compound (compound member) | _—_ |
| 2 | tā | **tā** | nominative feminine singular noun | _—_ |
| 3 | tuṣṭiḥ | **tuṣṭi** | nominative feminine singular noun | _—_ |
| 4 | tapaḥ | **tapas** | nominative neuter singular noun | _—_ |
| 5 | dānam | **dāna** | nominative neuter singular noun | _—_ |
| 6 | yaśaḥ | **yaśas** | nominative neuter singular noun | _—_ |
| 7 | ayaśaḥ | **ayaśas** | nominative neuter singular noun | _—_ |
| 8 | bhavanti | **bhū** | present indicative 3rd person plural verb | _—_ |
| 9 | bhāvāḥ | **bhāva** | nominative masculine plural noun | _—_ |
| 10 | bhūtānām | **bhūta** | genitive neuter plural noun | _—_ |
| 11 | mattaḥ | **mad** | ablative masculine singular noun | _—_ |
| 12 | eva | **eva** | — | _—_ |
| 13 | pṛthak | **pṛthak** | — | _—_ |
| 14 | vidhāḥ | **vidha** | nominative masculine plural noun | _—_ |


## BG 10.25 — Krishna

**Devanāgarī:** महर्षीणां भृगुर् अहं गिराम् अस्म्य् एकम् अक्षरम् | यज्ञानां जप-यज्ञो ऽस्मि स्थावराणां हिमालयः

**IAST:** *maharṣīṇāṃ bhṛgur ahaṃ girām asmy ekam akṣaram | yajñānāṃ japa-yajño 'smi sthāvarāṇāṃ himālayaḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | mahā | **mahat** | compound (compound member) | _maharṣi_ |
| 1 | ṛṣīṇām | **ṛṣi** | genitive masculine plural noun | _bhṛgu_ |
| 2 | bhṛguḥ | **bhṛgu** | nominative masculine singular noun | _aha_ |
| 3 | aham | **mad** | nominative singular noun | _gir_ |
| 4 | girām | **gir** | genitive feminine plural noun | _as_ |
| 5 | asmi | **as** | present indicative 1st person singular verb | _ej `nominative singular masculine noun`_ |
| 6 | ekam | **eka** | nominative neuter singular noun | _a `accusative singular masculine noun`_ |
| 7 | akṣaram | **akṣara** | nominative neuter singular noun | _kṣar_ |
| 8 | yajñānām | **yajña** | genitive masculine plural noun | _yaj_ |
| 9 | japa | **japa** | compound (compound member) | _jap_ |
| 10 | yajñaḥ | **yajña** | nominative masculine singular noun | _—_ |
| 11 | asmi | **as** | present indicative 1st person singular verb | _yaj_ |
| 12 | sthāvarāṇām | **sthāvara** | genitive masculine plural noun | _as_ |
| 13 | himālayaḥ | **himālaya** | nominative masculine singular noun | _sthāvara_ |
| 14 | himālayas | **—** | — | _himālaya_ |


## BG 11.6 — Krishna

**Devanāgarī:** पश्यादित्यान् वसून् रुद्रान् अश्विनौ मरुतस् तथा | बहून्य् अदृष्ट-पूर्वाणि पश्याश्चर्याणि भारत

**IAST:** *paśyādityān vasūn rudrān aśvinau marutas tathā | bahūny adṛṣṭa-pūrvāṇi paśyāścaryāṇi bhārata*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | paśya | **paś** | present imperative 2nd person singular verb | _dṛś_ |
| 1 | ādityān | **āditya** | accusative masculine plural noun | _a `ablative singular masculine noun`_ |
| 2 | vasūn | **vasu** | accusative masculine plural noun | _i `accusative plural masculine noun`_ |
| 3 | rudrān | **rudra** | accusative masculine plural noun | _av `nominative plural masculine noun`_ |
| 4 | aśvinau | **aśvin** | accusative masculine dual noun | _u `accusative plural masculine noun`_ |
| 5 | marutaḥ | **marut** | accusative masculine plural noun | _rudra_ |
| 6 | tathā | **tathā** | — | _aśvin_ |
| 7 | bahūni | **bahu** | accusative neuter plural noun | _marut_ |
| 8 | adṛṣṭa | **adṛṣṭa** | compound (compound member) | _tathā_ |
| 9 | pūrvāṇi | **pūrva** | accusative neuter plural noun | _bahu_ |
| 10 | paśya | **paś** | present imperative 2nd person singular verb | _u `accusative plural masculine noun`_ |
| 11 | āścaryāṇi | **āścarya** | accusative neuter plural noun | _i `nominative singular masculine noun`_ |
| 12 | bhārata | **bhārata** | vocative masculine singular noun | _ad `nominative singular masculine noun`_ |
| 13 | ṛṣṭa | **—** | — | _ṛṣ `vocative singular masculine noun`_ |
| 14 | - | **—** | — | _—_ |
| 15 | pūrvāṇi | **—** | — | _pūrv_ |
| 16 | paśya | **—** | — | _dṛś_ |
| 17 | as | **—** | — | _a `nominative singular masculine noun`_ |
| 18 | caryāṇi | **—** | — | _car_ |
| 19 | bhās | **—** | — | _bhū_ |
| 20 | rata | **—** | — | _ram_ |


## BG 11.19 — Krishna

**Devanāgarī:** अनादि-मध्यान्तम् अनन्त-वीर्यम् अनन्त-बाहुं शशि-सूर्य-नेत्रम् | पश्यामि त्वां दीप्त-हुताश-वक्त्रं स्व-तेजसा विश्वम् इदं तपन्तम्

**IAST:** *anādi-madhyāntam ananta-vīryam ananta-bāhuṃ śaśi-sūrya-netram | paśyāmi tvāṃ dīpta-hutāśa-vaktraṃ sva-tejasā viśvam idaṃ tapantam*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | anādi | **anādi** | compound (compound member) | _nad_ |
| 1 | madhya | **madhya** | compound (compound member) | _—_ |
| 2 | antam | **anta** | accusative masculine singular noun | _madhya_ |
| 3 | ananta | **ananta** | compound (compound member) | _anti_ |
| 4 | vīryam | **vīrya** | accusative masculine singular noun | _añji_ |
| 5 | ananta | **ananta** | compound (compound member) | _anti_ |
| 6 | bāhum | **bāhu** | accusative masculine singular noun | _—_ |
| 7 | śaśi | **śaśin** | compound (compound member) | _vīrya_ |
| 8 | sūrya | **sūrya** | compound (compound member) | _añji_ |
| 9 | netram | **netra** | accusative masculine singular noun | _anti_ |
| 10 | paśyāmi | **dṛś** | present indicative 1st person singular verb | _—_ |
| 11 | tvām | **tvad** | accusative singular noun | _bāhu_ |
| 12 | dīpta | **dīp** | compound participle (compound member) | _śaś_ |
| 13 | hutāśa | **hutāśa** | compound (compound member) | _—_ |
| 14 | vaktram | **vaktra** | accusative masculine singular noun | _sūrya_ |
| 15 | sva | **sva** | compound (compound member) | _—_ |
| 16 | tejasā | **tejas** | instrumental neuter singular noun | _nī `accusative singular masculine noun`_ |
| 17 | viśvam | **viśva** | accusative neuter singular noun | _dṛś_ |
| 18 | idam | **idam** | accusative neuter singular noun | _tva_ |
| 19 | tapantam | **tap** | accusative masculine singular present participle verb | _dīp_ |
| 20 | - | **—** | — | _—_ |
| 21 | hut | **—** | — | _hu `nominative singular masculine noun`_ |
| 22 | āśa | **—** | — | _aś_ |
| 23 | - | **—** | — | _—_ |
| 24 | vaktram | **—** | — | _vaktra_ |
| 25 | sva | **—** | — | _sva_ |
| 26 | - | **—** | — | _—_ |
| 27 | tā | **—** | — | _tan_ |
| 28 | ijas | **—** | — | _yaj_ |
| 29 | ās | **—** | — | _a `nominative plural masculine noun`_ |
| 30 | viśvam | **—** | — | _viśva_ |
| 31 | idam | **—** | — | _idam_ |
| 32 | tapantam | **—** | — | _tap_ |


## BG 11.53 — Krishna

**Devanāgarī:** नाहं वेदैर् न तपसा न दानेन न चेज्यया | शक्य एवं-विधो द्रष्टुं दृष्टवान् असि मां यथा

**IAST:** *nāhaṃ vedair na tapasā na dānena na cejyayā | śakya evaṃ-vidho draṣṭuṃ dṛṣṭavān asi māṃ yathā*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | na | **na** | — | _—_ |
| 1 | aham | **mad** | nominative singular noun | _—_ |
| 2 | vedaiḥ | **veda** | instrumental masculine plural noun | _—_ |
| 3 | na | **na** | — | _—_ |
| 4 | tapasā | **tapas** | instrumental neuter singular noun | _—_ |
| 5 | na | **na** | — | _—_ |
| 6 | dānena | **dāna** | instrumental neuter singular noun | _—_ |
| 7 | na | **na** | — | _—_ |
| 8 | ca | **ca** | — | _—_ |
| 9 | ijyayā | **ijyā** | instrumental feminine singular noun | _—_ |
| 10 | śakyaḥ | **śakya** | nominative masculine singular noun | _—_ |
| 11 | evaṃvidhaḥ | **evaṃvidha** | nominative masculine singular noun | _—_ |
| 12 | draṣṭum | **dṛś** | infinitive | _—_ |
| 13 | dṛṣṭavān | **dṛś** | nominative masculine singular participle noun | _—_ |
| 14 | asi | **as** | present indicative 2nd person singular verb | _—_ |
| 15 | mām | **mad** | accusative singular noun | _—_ |
| 16 | yathā | **yathā** | — | _—_ |


## BG 12.3 — Krishna

**Devanāgarī:** ये त्व् अक्षरम् अनिर्देश्यम् अव्यक्तं पर्युपासते | सर्वत्र-गम् अचिन्त्यं च कूटस्थम् अचलं ध्रुवम्

**IAST:** *ye tv akṣaram anirdeśyam avyaktaṃ paryupāsate | sarvatra-gam acintyaṃ ca kūṭastham acalaṃ dhruvam*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | ye | **yad** | nominative masculine plural noun | _yā `locative singular neuter noun`_ |
| 1 | tu | **tu** | — | _tu `nominative singular masculine noun`_ |
| 2 | akṣaram | **akṣara** | accusative neuter singular noun | _kṣar_ |
| 3 | anirdeśyam | **anirdeśya** | accusative neuter singular noun | _anirdeśya_ |
| 4 | avyaktam | **avyakta** | accusative neuter singular noun | _avyakta_ |
| 5 | paryupāsate | **paryupās** | present indicative 3rd person plural verb | _pari_ |
| 6 | sarvatra | **sarvatra** | — | _vap_ |
| 7 | gam | **ga** | accusative neuter singular noun | _as_ |
| 8 | acintyam | **acintya** | accusative neuter singular noun | _sa `nominative singular masculine noun`_ |
| 9 | ca | **ca** | — | _ru `nominative dual masculine noun`_ |
| 10 | kūṭastham | **kūṭastha** | accusative neuter singular noun | _atra_ |
| 11 | acalam | **acala** | accusative neuter singular noun | _—_ |
| 12 | dhruvam | **dhruva** | accusative neuter singular noun | _ga `accusative singular masculine noun`_ |
| 13 | acintyam | **—** | — | _acintya_ |
| 14 | ca | **—** | — | _ca `vocative singular masculine noun`_ |
| 15 | kūṭastham | **—** | — | _kūṭastha_ |
| 16 | acalam | **—** | — | _cal_ |
| 17 | dhruvam | **—** | — | _dhru_ |


## BG 12.17 — Krishna

**Devanāgarī:** यो न हृष्यति न द्वेष्टि न शोचति न काङ्क्षति | शुभाशुभ-परित्यागी भक्तिमान् यः स मे प्रियः

**IAST:** *yo na hṛṣyati na dveṣṭi na śocati na kāṅkṣati | śubhāśubha-parityāgī bhaktimān yaḥ sa me priyaḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | yaḥ | **yad** | nominative masculine singular noun | _ī `nominative plural masculine noun`_ |
| 1 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 2 | hṛṣyati | **hṛṣ** | present indicative 3rd person singular verb | _hṛṣ_ |
| 3 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 4 | dveṣṭi | **dviṣ** | present indicative 3rd person singular verb | _dviṣ_ |
| 5 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 6 | śocati | **śuc** | present indicative 3rd person singular verb | _śuc_ |
| 7 | na | **na** | — | _na `vocative singular neuter noun`_ |
| 8 | kāṅkṣati | **kāṅkṣ** | present indicative 3rd person singular verb | _kāṅkṣ_ |
| 9 | śubha | **śubha** | compound (compound member) | _śubh_ |
| 10 | aśubha | **aśubha** | compound (compound member) | _aśubha_ |
| 11 | parityāgī | **parityāgin** | nominative masculine singular noun | _—_ |
| 12 | bhaktimān | **bhaktimat** | nominative masculine singular noun | _parityāgin_ |
| 13 | yaḥ | **yad** | nominative masculine singular noun | _bhañj_ |
| 14 | sa | **tad** | nominative masculine singular noun | _a `accusative plural masculine noun`_ |
| 15 | me | **mad** | genitive singular noun | _ī `nominative plural masculine noun`_ |
| 16 | priyaḥ | **priya** | nominative masculine singular noun | _sa `vocative singular masculine noun`_ |
| 17 | me | **—** | — | _mā `locative singular neuter noun`_ |
| 18 | priyas | **—** | — | _prī_ |


## BG 12.19 — Krishna

**Devanāgarī:** तुल्य-निन्दा-स्तुतिर् मौनी संतुष्टो येन केनचित् | अनिकेतः स्थिर-मतिर् भक्तिमान् मे प्रियो नरः

**IAST:** *tulya-nindā-stutir maunī saṃtuṣṭo yena kenacit | aniketaḥ sthira-matir bhaktimān me priyo naraḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | tulya | **tulya** | compound (compound member) | _tulya_ |
| 1 | nindā | **nindā** | compound (compound member) | _—_ |
| 2 | stutiḥ | **stuti** | nominative masculine singular noun | _nind_ |
| 3 | maunī | **maunin** | nominative masculine singular noun | _—_ |
| 4 | saṃtuṣṭaḥ | **saṃtuṣ** | nominative masculine singular participle noun | _stu_ |
| 5 | yena | **yad** | instrumental neuter singular noun | _mā `vocative singular neuter noun`_ |
| 6 | kenacid | **kaścit** | instrumental neuter singular noun | _a `nominative singular masculine noun`_ |
| 7 | aniketaḥ | **aniketa** | nominative masculine singular noun | _ni `nominative dual masculine noun`_ |
| 8 | sthira | **sthira** | compound (compound member) | _saṃtuṣ_ |
| 9 | matiḥ | **mati** | nominative masculine singular noun | _yā `instrumental singular masculine noun`_ |
| 10 | bhaktimān | **bhaktimat** | nominative masculine singular noun | _—_ |
| 11 | me | **mad** | genitive singular noun | _aniketa_ |
| 12 | priyaḥ | **priya** | nominative masculine singular noun | _sthira_ |
| 13 | naraḥ | **nara** | nominative masculine singular noun | _—_ |
| 14 | matis | **—** | — | _man_ |
| 15 | bhaktim | **—** | — | _bhañj_ |
| 16 | ān | **—** | — | _a `accusative plural masculine noun`_ |
| 17 | me | **—** | — | _mā `locative singular neuter noun`_ |
| 18 | priyas | **—** | — | _prī_ |
| 19 | naras | **—** | — | _nṛ `nominative plural masculine noun`_ |


## BG 13.18 — Krishna

**Devanāgarī:** इति क्षेत्रं तथा ज्ञानं ज्ञेयं चोक्तं समासतः | मद्-भक्त एतद् विज्ञाय मद्-भावायोपपद्यते

**IAST:** *iti kṣetraṃ tathā jñānaṃ jñeyaṃ coktaṃ samāsataḥ | mad-bhakta etad vijñāya mad-bhāvāyopapadyate*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | iti | **iti** | — | _—_ |
| 1 | kṣetram | **kṣetra** | nominative neuter singular noun | _—_ |
| 2 | tathā | **tathā** | — | _—_ |
| 3 | jñānam | **jñāna** | nominative neuter singular noun | _—_ |
| 4 | jñeyam | **jñā** | nominative neuter singular gdv noun | _—_ |
| 5 | ca | **ca** | — | _—_ |
| 6 | uktam | **vac** | nominative neuter singular participle noun | _—_ |
| 7 | samāsatas | **samāsatas** | — | _—_ |
| 8 | mad | **mad** | compound (compound member) | _—_ |
| 9 | bhaktaḥ | **bhakta** | nominative masculine singular noun | _—_ |
| 10 | etat | **etad** | accusative neuter singular noun | _—_ |
| 11 | vijñāya | **vijñā** | conv | _—_ |
| 12 | mad | **mad** | compound (compound member) | _—_ |
| 13 | bhāvāya | **bhāva** | dative masculine singular noun | _—_ |
| 14 | upapadyate | **upapad** | present indicative 3rd person singular verb | _—_ |


## BG 13.21 — Krishna

**Devanāgarī:** पुरुषः प्रकृति-स्थो हि भुङ्क्ते प्रकृतिजान् गुणान् | कारणं गुण-सङ्गो ऽस्य सद्-असद्-योनि-जन्मसु

**IAST:** *puruṣaḥ prakṛti-stho hi bhuṅkte prakṛtijān guṇān | kāraṇaṃ guṇa-saṅgo 'sya sad-asad-yoni-janmasu*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | puruṣaḥ | **puruṣa** | nominative masculine singular noun | _—_ |
| 1 | prakṛti | **prakṛti** | compound feminine (compound member) | _—_ |
| 2 | sthaḥ | **stha** | nominative masculine singular noun | _—_ |
| 3 | hi | **hi** | — | _—_ |
| 4 | bhuṅkte | **bhuj** | present indicative 3rd person singular verb | _—_ |
| 5 | prakṛti | **prakṛti** | compound (compound member) | _—_ |
| 6 | jān | **ja** | accusative masculine plural noun | _—_ |
| 7 | guṇān | **guṇa** | accusative masculine plural noun | _—_ |
| 8 | kāraṇam | **kāraṇa** | nominative neuter singular noun | _—_ |
| 9 | guṇa | **guṇa** | compound (compound member) | _—_ |
| 10 | saṅgaḥ | **saṅga** | nominative masculine singular noun | _—_ |
| 11 | asya | **idam** | genitive masculine singular noun | _—_ |
| 12 | sat | **as** | compound present participle (compound member) | _—_ |
| 13 | asat | **asat** | compound (compound member) | _—_ |
| 14 | yoni | **yoni** | compound (compound member) | _—_ |
| 15 | janmasu | **janman** | locative neuter plural noun | _—_ |


## BG 13.29 — Krishna

**Devanāgarī:** प्रकृत्यैव च कर्माणि क्रियमाणानि सर्वशः | यः पश्यति तथात्मानम् अकर्तारं स पश्यति

**IAST:** *prakṛtyaiva ca karmāṇi kriyamāṇāni sarvaśaḥ | yaḥ paśyati tathātmānam akartāraṃ sa paśyati*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | prakṛtyā | **prakṛti** | instrumental feminine singular noun | _prakṛ_ |
| 1 | eva | **eva** | — | _eva_ |
| 2 | ca | **ca** | — | _ca `vocative singular masculine noun`_ |
| 3 | karmāṇi | **karman** | accusative neuter plural noun | _karman_ |
| 4 | kriyamāṇāni | **kṛ** | accusative neuter plural present participle pass verb | _kṛ `nominative plural neuter noun`_ |
| 5 | sarvaśas | **sarvaśas** | — | _sarvaśas_ |
| 6 | yaḥ | **yad** | nominative masculine singular noun | _ī `nominative plural masculine noun`_ |
| 7 | paśyati | **dṛś** | present indicative 3rd person singular verb | _dṛś_ |
| 8 | tathā | **tathā** | — | _tathā_ |
| 9 | ātmānam | **ātman** | accusative masculine singular noun | _a `ablative singular masculine noun`_ |
| 10 | akartāram | **akartṛ** | accusative masculine singular noun | _mā `accusative singular masculine noun`_ |
| 11 | sa | **tad** | nominative masculine singular noun | _aj `nominative singular masculine noun`_ |
| 12 | paśyati | **dṛś** | present indicative 3rd person singular verb | _ṛ `accusative singular masculine noun`_ |
| 13 | sa | **—** | — | _sa `vocative singular masculine noun`_ |
| 14 | paśyati | **—** | — | _dṛś_ |


## BG 14.11 — Krishna

**Devanāgarī:** सर्व-द्वारेषु देहे ऽस्मिन् प्रकाश उपजायते | ज्ञानं यदा तदा विद्याद् विवृद्धं सत्त्वम् इत्य् उत

**IAST:** *sarva-dvāreṣu dehe 'smin prakāśa upajāyate | jñānaṃ yadā tadā vidyād vivṛddhaṃ sattvam ity uta*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | sarva | **sarva** | compound (compound member) | _sarva_ |
| 1 | dvāreṣu | **dvāra** | locative neuter plural noun | _—_ |
| 2 | dehe | **deha** | locative masculine singular noun | _dvāri_ |
| 3 | asmin | **idam** | locative masculine singular noun | _dah_ |
| 4 | prakāśaḥ | **prakāśa** | nominative masculine singular noun | _a `nominative singular masculine noun`_ |
| 5 | upajāyate | **upajan** | present indicative 3rd person singular verb | _mind_ |
| 6 | jñānam | **jñāna** | nominative neuter singular noun | _prakāśa_ |
| 7 | yadā | **yadā** | — | _upajan_ |
| 8 | tadā | **tadā** | — | _jñā_ |
| 9 | vidyāt | **vid** | present optative 3rd person singular verb | _yat_ |
| 10 | vivṛddham | **vivṛdh** | nominative neuter singular participle noun | _ā `instrumental singular masculine noun`_ |
| 11 | sattvam | **sattva** | nominative neuter singular noun | _tadā_ |
| 12 | iti | **iti** | — | _vid_ |
| 13 | uta | **uta** | — | _vivṛdh_ |
| 14 | sat | **—** | — | _sat_ |
| 15 | tvam | **—** | — | _tva_ |
| 16 | itī | **—** | — | _iti_ |
| 17 | uta | **—** | — | _u `vocative singular masculine noun`_ |


## BG 14.12 — Krishna

**Devanāgarī:** लोभः प्रवृत्तिर् आरम्भः कर्मणाम् अशमः स्पृहा | रजस्य् एतानि जायन्ते विवृद्धे भरतर्षभ

**IAST:** *lobhaḥ pravṛttir ārambhaḥ karmaṇām aśamaḥ spṛhā | rajasy etāni jāyante vivṛddhe bharatarṣabha*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | lobhaḥ | **lobha** | nominative masculine singular noun | _lubh_ |
| 1 | pravṛttiḥ | **pravṛtti** | nominative feminine singular noun | _pravṛt_ |
| 2 | ārambhaḥ | **ārambha** | nominative masculine singular noun | _ārambha_ |
| 3 | karmaṇām | **karman** | genitive neuter plural noun | _karman_ |
| 4 | aśamaḥ | **aśama** | nominative masculine singular noun | _śam_ |
| 5 | spṛhā | **spṛhā** | nominative feminine singular noun | _spṛhā_ |
| 6 | rajasi | **rajas** | locative neuter singular noun | _rajas_ |
| 7 | etāni | **etad** | nominative neuter plural noun | _etad_ |
| 8 | jāyante | **jan** | present indicative 3rd person plural verb | _jan_ |
| 9 | vivṛddhe | **vivṛdh** | locative neuter singular participle noun | _vivṛdh_ |
| 10 | bharata | **bharata** | compound (compound member) | _bharataṛṣabha_ |
| 11 | ṛṣabha | **ṛṣabha** | vocative masculine singular noun | _—_ |


## BG 14.20 — Krishna

**Devanāgarī:** गुणान् एतान् अतीत्य त्रीन् देही देह-समुद्भवान् | जन्म-मृत्यु-जरा-दुःखैर् विमुक्तो ऽमृतम् अश्नुते

**IAST:** *guṇān etān atītya trīn dehī deha-samudbhavān | janma-mṛtyu-jarā-duḥkhair vimukto 'mṛtam aśnute*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | guṇān | **guṇa** | accusative masculine plural noun | _guṇa_ |
| 1 | etān | **etad** | accusative masculine plural noun | _etad_ |
| 2 | atītya | **atī** | conv | _ati_ |
| 3 | trīn | **tri** | accusative masculine plural noun | _i `vocative singular masculine noun`_ |
| 4 | dehī | **dehin** | nominative masculine singular noun | _tri_ |
| 5 | deha | **deha** | compound (compound member) | _dih_ |
| 6 | samudbhavān | **samudbhava** | accusative masculine plural noun | _dih_ |
| 7 | janma | **janman** | compound (compound member) | _—_ |
| 8 | mṛtyu | **mṛtyu** | compound (compound member) | _samudbhava_ |
| 9 | jarā | **jarā** | compound (compound member) | _janman_ |
| 10 | duḥkhaiḥ | **duḥkha** | instrumental neuter plural noun | _—_ |
| 11 | vimuktaḥ | **vimuc** | nominative masculine singular participle noun | _mṛ `locative singular masculine noun`_ |
| 12 | amṛtam | **amṛta** | accusative neuter singular noun | _u `nominative singular masculine noun`_ |
| 13 | aśnute | **aś** | present indicative 3rd person singular verb | _—_ |
| 14 | jarā | **—** | — | _jṛ `nominative singular feminine noun`_ |
| 15 | - | **—** | — | _—_ |
| 16 | dus | **—** | — | _dus_ |
| 17 | khais | **—** | — | _khan_ |
| 18 | vimuktas | **—** | — | _vimuc_ |
| 19 | amṛtam | **—** | — | _amṛta_ |
| 20 | aśnute | **—** | — | _aś_ |


## BG 15.2 — Krishna

**Devanāgarī:** अधश् चोर्ध्वं प्रसृतास् तस्य शाखा गुण-प्रवृद्धा विषय-प्रवालाः | अधश् च मूलान्य् अनुसंततानि कर्मानुबन्धीनि मनुष्य-लोके

**IAST:** *adhaś cordhvaṃ prasṛtās tasya śākhā guṇa-pravṛddhā viṣaya-pravālāḥ | adhaś ca mūlāny anusaṃtatāni karmānubandhīni manuṣya-loke*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | adhas | **adhas** | — | _adhas_ |
| 1 | ca | **ca** | — | _ca `vocative singular masculine noun`_ |
| 2 | ūrdhvam | **ūrdhvam** | — | _ūrdhvam_ |
| 3 | prasṛtāḥ | **prasṛ** | nominative feminine plural participle noun | _prasṛ_ |
| 4 | tasya | **tad** | genitive masculine singular noun | _tad_ |
| 5 | śākhāḥ | **śākhā** | nominative feminine plural noun | _śākhā_ |
| 6 | guṇa | **guṇa** | compound (compound member) | _guṇa_ |
| 7 | pravṛddhāḥ | **pravṛdh** | nominative feminine plural participle noun | _—_ |
| 8 | viṣaya | **viṣaya** | compound (compound member) | _pravṛt_ |
| 9 | pravālāḥ | **pravāla** | nominative feminine plural noun | _ha `nominative plural masculine noun`_ |
| 10 | adhas | **adhas** | — | _viṣaya_ |
| 11 | ca | **ca** | — | _—_ |
| 12 | mūlāni | **mūla** | nominative neuter plural noun | _pravāla_ |
| 13 | anusaṃtatāni | **anusaṃtan** | nominative neuter plural participle noun | _adhas_ |
| 14 | karma | **karman** | compound (compound member) | _ca `vocative singular masculine noun`_ |
| 15 | anubandhīni | **anubandhin** | nominative neuter plural noun | _mūli_ |
| 16 | manuṣya | **manuṣya** | compound (compound member) | _anu_ |
| 17 | loke | **loka** | locative masculine singular noun | _a `accusative singular masculine noun`_ |
| 18 | tatāni | **—** | — | _tan_ |
| 19 | karma | **—** | — | _karman_ |
| 20 | anubandhīni | **—** | — | _anubandhin_ |
| 21 | manuṣi | **—** | — | _manus_ |
| 22 | a | **—** | — | _a `vocative singular masculine noun`_ |
| 23 | - | **—** | — | _—_ |
| 24 | loke | **—** | — | _lok_ |


## BG 15.8 — Krishna

**Devanāgarī:** शरीरं यद् अवाप्नोति यच् चाप्य् उत्क्रामतीश्वरः | गृहीत्वैतानि संयाति वायुर् गन्धान् इवाशयात्

**IAST:** *śarīraṃ yad avāpnoti yac cāpy utkrāmatīśvaraḥ | gṛhītvaitāni saṃyāti vāyur gandhān ivāśayāt*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | śarīram | **śarīra** | accusative neuter singular noun | _śarīra_ |
| 1 | yat | **yad** | accusative neuter singular noun | _yat_ |
| 2 | avāpnoti | **avāp** | present indicative 3rd person singular verb | _u `vocative singular masculine noun`_ |
| 3 | yat | **yad** | accusative neuter singular noun | _āp_ |
| 4 | ca | **ca** | — | _yat_ |
| 5 | api | **api** | — | _ca `vocative singular masculine noun`_ |
| 6 | utkrāmati | **utkram** | present indicative 3rd person singular verb | _api_ |
| 7 | īśvaraḥ | **īśvara** | nominative masculine singular noun | _utkram_ |
| 8 | gṛhītvā | **grah** | conv | _īśvara_ |
| 9 | etāni | **etad** | accusative neuter plural noun | _grah_ |
| 10 | saṃyāti | **saṃyā** | present indicative 3rd person singular verb | _etad_ |
| 11 | vāyuḥ | **vāyu** | nominative masculine singular noun | _saṃyā_ |
| 12 | gandhān | **gandha** | accusative masculine plural noun | _vāyu_ |
| 13 | iva | **iva** | — | _gandha_ |
| 14 | āśayāt | **āśaya** | ablative masculine singular noun | _iva_ |
| 15 | āśayāt | **—** | — | _āśī_ |


## BG 15.12 — Krishna

**Devanāgarī:** यद् आदित्य-गतं तेजो जगद् भासयते ऽखिलम् | यच् चन्द्रमसि यच् चाग्नौ तत् तेजो विद्धि मामकम्

**IAST:** *yad āditya-gataṃ tejo jagad bhāsayate 'khilam | yac candramasi yac cāgnau tat tejo viddhi māmakam*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | yat | **yad** | nominative neuter singular noun | _yat_ |
| 1 | āditya | **āditya** | compound (compound member) | _a `ablative singular masculine noun`_ |
| 2 | gatam | **gam** | nominative neuter singular participle noun | _i `vocative singular masculine noun`_ |
| 3 | tejaḥ | **tejas** | nominative neuter singular noun | _—_ |
| 4 | jagat | **jagant** | accusative neuter singular noun | _gam_ |
| 5 | bhāsayate | **bhāsay** | present indicative 3rd person singular verb | _tan_ |
| 6 | akhilam | **akhila** | accusative neuter singular noun | _yaj_ |
| 7 | yat | **yad** | nominative neuter singular noun | _jagat_ |
| 8 | candramasi | **candramas** | locative masculine singular noun | _bhū_ |
| 9 | yat | **yad** | nominative neuter singular noun | _yat_ |
| 10 | ca | **ca** | — | _akhila_ |
| 11 | agnau | **agni** | locative masculine singular noun | _yat_ |
| 12 | tat | **tad** | accusative neuter singular noun | _candra_ |
| 13 | tejaḥ | **tejas** | accusative neuter singular noun | _as_ |
| 14 | viddhi | **vid** | present imperative 2nd person singular verb | _yat_ |
| 15 | māmakam | **māmaka** | accusative neuter singular noun | _ca `nominative plural masculine noun`_ |
| 16 | gnā | **—** | — | _gnā_ |
| 17 | au | **—** | — | _a `nominative dual masculine noun`_ |
| 18 | tat | **—** | — | _tad_ |
| 19 | tā | **—** | — | _tan_ |
| 20 | ijas | **—** | — | _yaj_ |
| 21 | viddhi | **—** | — | _vid_ |
| 22 | mām | **—** | — | _mā `Vibhakti.Sasthi plural neuter noun`_ |
| 23 | akam | **—** | — | _aka_ |


## BG 16.5 — Krishna

**Devanāgarī:** दैवी संपद् विमोक्षाय निबन्धायासुरी मता | मा शुचः संपदं दैवीम् अभिजातो ऽसि पाण्डव

**IAST:** *daivī saṃpad vimokṣāya nibandhāyāsurī matā | mā śucaḥ saṃpadaṃ daivīm abhijāto 'si pāṇḍava*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | daivī | **daiva** | nominative feminine singular noun | _daivī_ |
| 1 | saṃpad | **sampad** | nominative feminine singular noun | _sa `accusative singular masculine noun`_ |
| 2 | vimokṣāya | **vimokṣa** | dative masculine singular noun | _pat_ |
| 3 | nibandhāya | **nibandha** | dative masculine singular noun | _vimokṣa_ |
| 4 | āsurī | **āsura** | nominative feminine singular noun | _nibandh_ |
| 5 | matā | **man** | nominative feminine singular participle noun | _u `nominative singular masculine noun`_ |
| 6 | mā | **mā** | — | _i `nominative dual masculine noun`_ |
| 7 | śucaḥ | **śuc** | past jus 2nd person singular verb | _man_ |
| 8 | saṃpadam | **sampad** | accusative feminine singular noun | _mā `vocative singular neuter noun`_ |
| 9 | daivīm | **daiva** | accusative feminine singular noun | _śuc_ |
| 10 | abhijātaḥ | **abhijan** | nominative masculine singular participle noun | _sa `accusative singular masculine noun`_ |
| 11 | asi | **as** | present indicative 2nd person singular verb | _pad_ |
| 12 | pāṇḍava | **pāṇḍava** | vocative masculine singular noun | _daivī_ |
| 13 | abhijātas | **—** | — | _abhijan_ |
| 14 | asi | **—** | — | _as_ |
| 15 | pāṇḍava | **—** | — | _pāṇḍava_ |


## BG 16.10 — Krishna

**Devanāgarī:** कामम् आश्रित्य दुष्पूरं दम्भ-मान-मदान्विताः | मोहाद् गृहीत्वासद्-ग्राहान् प्रवर्तन्ते ऽशुचिव्रताः

**IAST:** *kāmam āśritya duṣpūraṃ dambha-māna-madānvitāḥ | mohād gṛhītvāsad-grāhān pravartante 'śucivratāḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | kāmam | **kāma** | accusative masculine singular noun | _—_ |
| 1 | āśritya | **āśri** | conv | _—_ |
| 2 | duṣpūram | **duṣpūra** | accusative masculine singular noun | _—_ |
| 3 | dambha | **dambha** | compound (compound member) | _—_ |
| 4 | māna | **māna** | compound (compound member) | _—_ |
| 5 | mada | **mada** | compound (compound member) | _—_ |
| 6 | anvitāḥ | **anvita** | nominative masculine plural noun | _—_ |
| 7 | mohāt | **moha** | ablative masculine singular noun | _—_ |
| 8 | gṛhītvā | **grah** | conv | _—_ |
| 9 | asat | **asat** | compound (compound member) | _—_ |
| 10 | grāhān | **grāha** | accusative masculine plural noun | _—_ |
| 11 | pravartante | **pravṛt** | present indicative 3rd person plural verb | _—_ |
| 12 | aśuci | **aśuci** | compound (compound member) | _—_ |
| 13 | vratāḥ | **vrata** | nominative masculine plural noun | _—_ |


## BG 16.17 — Krishna

**Devanāgarī:** आत्म-संभाविताः स्तब्धा धन-मान-मदान्विताः | यजन्ते नाम-यज्ञैस् ते दम्भेनाविधि-पूर्वकम्

**IAST:** *ātma-saṃbhāvitāḥ stabdhā dhana-māna-madānvitāḥ | yajante nāma-yajñais te dambhenāvidhi-pūrvakam*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | ātma | **ātman** | compound (compound member) | _a `ablative singular masculine noun`_ |
| 1 | saṃbhāvitāḥ | **sambhāvay** | nominative masculine plural participle noun | _ma `vocative singular masculine noun`_ |
| 2 | stabdhāḥ | **stambh** | nominative masculine plural participle noun | _—_ |
| 3 | dhana | **dhana** | compound (compound member) | _sa `accusative singular masculine noun`_ |
| 4 | māna | **māna** | compound (compound member) | _bhū_ |
| 5 | mada | **mada** | compound (compound member) | _stambh_ |
| 6 | anvitāḥ | **anvita** | nominative masculine plural noun | _dhana_ |
| 7 | yajante | **yaj** | present indicative 3rd person plural verb | _—_ |
| 8 | nāma | **nāman** | compound (compound member) | _mā `vocative singular masculine noun`_ |
| 9 | yajñaiḥ | **yajña** | instrumental masculine plural noun | _—_ |
| 10 | te | **tad** | nominative masculine plural noun | _mad_ |
| 11 | dambhena | **dambha** | instrumental masculine singular noun | _anvi_ |
| 12 | a | **a** | — | _yaj_ |
| 13 | vidhi | **vidhi** | compound (compound member) | _nāma_ |
| 14 | pūrvakam | **pūrvaka** | accusative neuter singular noun | _—_ |
| 15 | yajñais | **—** | — | _yaj_ |
| 16 | te | **—** | — | _tā `nominative dual feminine noun`_ |
| 17 | dambhena | **—** | — | _dambha_ |
| 18 | āvidhi | **—** | — | _āvyadh_ |
| 19 | - | **—** | — | _—_ |
| 20 | pūrvakam | **—** | — | _pūrvaka_ |


## BG 17.5 — Krishna

**Devanāgarī:** अशास्त्र-विहितं घोरं तप्यन्ते ये तपो जनाः | दम्भाहंकार-संयुक्ताः काम-राग-बलान्विताः

**IAST:** *aśāstra-vihitaṃ ghoraṃ tapyante ye tapo janāḥ | dambhāhaṃkāra-saṃyuktāḥ kāma-rāga-balānvitāḥ*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | a | **a** | — | _aś `vocative singular masculine noun`_ |
| 1 | śāstra | **śāstra** | compound (compound member) | _astra_ |
| 2 | vihitam | **vidhā** | accusative neuter singular participle noun | _—_ |
| 3 | ghoram | **ghora** | accusative neuter singular noun | _vidhā_ |
| 4 | tapyante | **tap** | present indicative pass 3rd person plural verb | _ghora_ |
| 5 | ye | **yad** | nominative masculine plural noun | _tap_ |
| 6 | tapaḥ | **tapas** | accusative neuter singular noun | _yā `locative singular neuter noun`_ |
| 7 | janāḥ | **jana** | nominative masculine plural noun | _tap_ |
| 8 | dambha | **dambha** | compound (compound member) | _jana_ |
| 9 | ahaṃkāra | **ahaṃkāra** | compound (compound member) | _dambha_ |
| 10 | saṃyuktāḥ | **saṃyuj** | nominative masculine plural participle noun | _ha `accusative singular masculine noun`_ |
| 11 | kāma | **kāma** | compound (compound member) | _kṛ `vocative singular masculine noun`_ |
| 12 | rāga | **rāga** | compound (compound member) | _—_ |
| 13 | bala | **bala** | compound (compound member) | _saṃyuj_ |
| 14 | anvitāḥ | **anvita** | nominative masculine plural noun | _kāma_ |
| 15 | - | **—** | — | _—_ |
| 16 | rāga | **—** | — | _rāj_ |
| 17 | - | **—** | — | _—_ |
| 18 | balā | **—** | — | _balā_ |
| 19 | anvitās | **—** | — | _anvi_ |


## BG 17.22 — Krishna

**Devanāgarī:** अदेश-काले यद् दानम् अपात्रेभ्यश् च दीयते | असत्कृतम् अवज्ञातं तत् तामसम् उदाहृतम्

**IAST:** *adeśa-kāle yad dānam apātrebhyaś ca dīyate | asatkṛtam avajñātaṃ tat tāmasam udāhṛtam*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | a | **a** | — | _ad `vocative singular masculine noun`_ |
| 1 | deśa | **deśa** | compound (compound member) | _īś `vocative singular masculine noun`_ |
| 2 | kāle | **kāla** | locative masculine singular noun | _—_ |
| 3 | yat | **yad** | nominative neuter singular noun | _kal_ |
| 4 | dānam | **dāna** | nominative neuter singular noun | _yat_ |
| 5 | apātrebhyaḥ | **apātra** | dative masculine plural noun | _dā `accusative singular masculine noun`_ |
| 6 | ca | **ca** | — | _apa_ |
| 7 | dīyate | **dā** | present indicative pass 3rd person singular verb | _atra_ |
| 8 | asatkṛtam | **asatkṛ** | nominative neuter singular participle noun | _ca `vocative singular masculine noun`_ |
| 9 | avajñātam | **avajñā** | nominative neuter singular participle noun | _dā_ |
| 10 | tat | **tad** | nominative neuter singular noun | _as `nominative singular neuter noun`_ |
| 11 | tāmasam | **tāmasa** | nominative neuter singular noun | _kṛ `accusative singular masculine noun`_ |
| 12 | udāhṛtam | **udāhṛ** | nominative neuter singular participle noun | _avajñā_ |
| 13 | tat | **—** | — | _tad_ |
| 14 | tāmasam | **—** | — | _tāmasa_ |
| 15 | udāhṛtam | **—** | — | _udāhṛ_ |


## BG 18.23 — Krishna

**Devanāgarī:** नियतं सङ्गरहितमरागद्वेषतः कृतम् | अफलप्रेप्सुना कर्म यत्तत्सात्त्विकमुच्यते

**IAST:** *niyataṃ saṅgarahitamarāgadveṣataḥ kṛtam | aphalaprepsunā karma yattatsāttvikamucyate*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | niyatam | **niyam** | nominative neuter singular participle noun | _niyam_ |
| 1 | saṅga | **saṅga** | compound (compound member) | _—_ |
| 2 | rahitam | **rahita** | nominative neuter singular noun | _kṛ `accusative singular masculine noun`_ |
| 3 | a | **a** | — | _aphalaprepsu_ |
| 4 | rāga | **rāga** | compound (compound member) | _karman_ |
| 5 | dveṣataḥ | **dveṣa** | ablative masculine singular noun | _—_ |
| 6 | kṛtam | **kṛ** | nominative neuter singular participle noun | _—_ |
| 7 | a | **a** | — | _—_ |
| 8 | phala | **phala** | compound (compound member) | _—_ |
| 9 | prepsunā | **prepsu** | instrumental masculine singular noun | _—_ |
| 10 | karma | **karman** | nominative neuter singular noun | _—_ |
| 11 | yat | **yad** | nominative neuter singular noun | _—_ |
| 12 | tat | **tad** | nominative neuter singular noun | _—_ |
| 13 | sāttvikam | **sāttvika** | nominative neuter singular noun | _—_ |
| 14 | ucyate | **vac** | present indicative pass 3rd person singular verb | _—_ |


## BG 18.71 — Krishna

**Devanāgarī:** श्रद्धावाननसूयश्च शृणुयादपि यो नरः | सोऽपि मुक्तः शुभा~ल्लोकान्प्राप्नुयात्पुण्यकर्मणाम्

**IAST:** *śraddhāvānanasūyaśca śṛṇuyādapi yo naraḥ | so'pi muktaḥ śubhā~llokānprāpnuyātpuṇyakarmaṇām*


| # | surface | multitask lemma | multitask morph | vidyut lemma (contrast only) |
|--:|:--|:--|:--|:--|
| 0 | śraddhāvān | **śraddhāvat** | nominative masculine singular noun | _śraddhā_ |
| 1 | anasūyaḥ | **anasūya** | nominative masculine singular noun | _vā `nominative singular masculine noun`_ |
| 2 | ca | **ca** | — | _anasūya_ |
| 3 | śṛṇuyāt | **śru** | present optative 3rd person singular verb | _ca `vocative singular masculine noun`_ |
| 4 | api | **api** | — | _śru_ |
| 5 | yaḥ | **yad** | nominative masculine singular noun | _api_ |
| 6 | naraḥ | **nara** | nominative masculine singular noun | _ī `nominative plural masculine noun`_ |
| 7 | saḥ | **tad** | nominative masculine singular noun | _nṛ `nominative plural masculine noun`_ |
| 8 | api | **api** | — | _sa `nominative singular masculine noun`_ |
| 9 | muktaḥ | **muc** | nominative masculine singular participle noun | _api_ |
| 10 | śubhān | **śubha** | accusative masculine plural noun | _muc_ |
| 11 | lokān | **loka** | accusative masculine plural noun | _śubh_ |
| 12 | prāpnuyāt | **prāp** | present optative 3rd person singular verb | _—_ |
| 13 | puṇya | **puṇya** | compound (compound member) | _—_ |
| 14 | karmaṇām | **karman** | genitive masculine plural noun | _—_ |


---

## Scoring

When done, count: total multitask rows, rows you marked `✗`, rows you marked `morph:✗`. Lemma-agreement = 1 − (lemma_✗ / total). Morph-agreement = 1 − (morph_✗ / total). Validation gate is ≥95% lemma-agreement to un-hide the word-by-word section across the 700-verse site.
