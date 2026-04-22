# Substrate parser eval — meaning-first review sheet

**What you are doing:** scanning whether the new Sanskrit parser correctly identifies the words inside each verse.

**What is on each verse:**
1. The verse in IAST so you can read it.
2. Śaṅkara's English rendering — so you know what the verse means.
3. **A list of words the parser found**, each with the parser-lemma + a 1-line dictionary gloss (Monier-Williams).

**What you are looking for:** rows where the parser-lemma is *clearly wrong for this verse* — meaning, the dictionary gloss has nothing to do with what the verse needs. Mark those `→ X`.

**Two failure modes to distinguish:**
- `→ X parser` — the parser identified the wrong word (e.g., it returned `eka` where the verse needs `āyus`).
- `→ X gloss` — the parser is right but the dictionary returned the wrong entry for a homonym (e.g., `ca` shown as the consonant-letter ca rather than the conjunction "and"). This is NOT a parser error; it tells me to fix the gloss-fetcher.

If a row looks right, or you cannot judge, leave it alone.

**Time:** 50 verses, ~756 words. If the first 10 verses look mostly clean, the substrate is publishable — stop early. If the first 10 are full of errors, also stop and tell me.

---

## BG 1.16

_ananta-vijayaṃ rājā kuntī-putro yudhiṣṭhiraḥ | nakulaḥ sahadevaś ca sughoṣa-maṇipuṣpakau_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The twin sons of Pāṇḍu — Nakula and Sahadeva — blew their conches, named Sughoṣa (well-sounding) and Maṇipuṣpaka (jewel-blossomed); and the king Yudhiṣṭhira, son of Kuntī, blew Anantavijaya (endless victory). These are mere names for instruments in the unfolding spectacle of saṃsāra (the turning wheel of conditioned existence). For Śaṅkara the significance of this verse lies entirely in what it does not say: the Self (ātman) that will soon be invoked at 2.11 is not here, not yet — only the parade of embodied warriors sounding their attachment to a world the jñānin (knower) must ultimately reno…


**Words the parser found:**

- **ananta** _(seen as ananta)_ — _(no MW gloss; not in dictionary)_
- **vijaya** _(seen as vijayam)_ — year of Jupiter's cycle, VarBṛS
- **rājan** _(seen as rājā)_ — in Tat-puruṣa s
- **kuntī** _(seen as kuntī)_ — _(no MW gloss; not in dictionary)_
- **putra** _(seen as putraḥ)_ — a son, child, (also the young of an animal
- **yudhiṣṭhira** _(seen as yudhiṣṭhiraḥ)_ — _(no MW gloss; not in dictionary)_
- **nakula** _(seen as nakulaḥ)_ — of a partic. colour (perhaps that of the ichneumon), TS
- **sahadeva** _(seen as sahadevaḥ)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **sughoṣa** _(seen as sughoṣa)_ — _(no MW gloss; not in dictionary)_
- **maṇipuṣpaka** _(seen as maṇipuṣpakau)_ — _(no MW gloss; not in dictionary)_


## BG 1.46

_yadi mām apratīkāram aśastraṃ śastra-pāṇayaḥ | dhārtarāṣṭrā raṇe hanyus tan me kṣemataraṃ bhavet_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Arjuna declares that if the sons of Dhṛtarāṣṭra (dhārtarāṣṭrāḥ) were to slay him unresisting and weaponless (apratīkāram aśastram), that would constitute a greater good (kṣemataram) for him than participating in the slaughter. From an Advaita standpoint, this utterance marks the precise moment of viveka's (discriminative intelligence's) inversion — the very faculty meant to distinguish ātman from anātman here confuses kinship-obligation with self-preservation, producing the illusion that death is preferable to dharmic action. The verse is the nadir of moha (delusion); Kṛṣṇa's silence here sign…


**Words the parser found:**

- **yadi** _(seen as yadi)_ — if, in case that, In the earlier language yadi may be joined with Indic. Subj. or Leṭ Pot. , or…
- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **apratīkāra** _(seen as apratīkāram)_ — _(no MW gloss; not in dictionary)_
- **aśastra** _(seen as aśastram)_ — _(no MW gloss; not in dictionary)_
- **śastra** _(seen as śastra)_ — _(no MW gloss; not in dictionary)_
- **pāṇi** _(seen as pāṇayaḥ)_ — _(no MW gloss; not in dictionary)_
- **dhārtarāṣṭra** _(seen as dhārtarāṣṭrāḥ)_ — _(no MW gloss; not in dictionary)_
- **raṇa** _(seen as raṇe)_ — _(no MW gloss; not in dictionary)_
- **han** _(seen as hanyuḥ)_ — hanti (3. du. hataH , 3. pl. Gnanti
- **tad** _(seen as tat)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **kṣematara** _(seen as kṣemataram)_ — _(no MW gloss; not in dictionary)_
- **bhū** _(seen as bhavet)_ — Bavati (rarely Ā. °te


## BG 2.12

_kutas te aśocyāḥ ? yato nityāḥ | katham ? na tv evāhaṃ jātu nāsaṃ na tvaṃ neme janādhipāḥ | na caiva na bhaviṣyāmaḥ sarve vayam ataḥ param_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Never was there a time when I did not exist — I always was, just as ākāśa (space) persists unchanged through the arising and perishing of pots and jars. The plural pronouns — 'I,' 'you,' 'these kings' — track the succession of bodies, not any real multiplicity of ātman; as the bhāṣya states, the plural follows the difference of bodies, not the intent of difference among ātmans (dehabhedānuvṛttyā bahuvacanam, nātmabhedābhiprāyeṇa). In all three times — past, present, future — the one ātman-svarūpa (the nature of the Self itself) is eternal, and grief over its supposed birth or death is founded …


**Words the parser found:**

- **kutas** _(seen as kutas)_ — from no side
- **tad** _(seen as te)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **aśocya** _(seen as aśocyāḥ)_ — _(no MW gloss; not in dictionary)_
- **yatas** _(seen as yatas)_ — from which or what, whence, whereof, wherefrom, ( yato yataH , ‘from whichever’, ‘from whatever’,…
- **nitya** _(seen as nityāḥ)_ — innate, native, iii, 13941
- **katham** _(seen as katham)_ — _(no MW gloss; not in dictionary)_
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **tu** _(seen as tu)_ — to have authority, be strong, i, 94, 2 ( pf. tUtAva Naigh. iv, 1
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **mad** _(seen as aham)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **jātu** _(seen as jātu)_ — at all, ever, x, 27, 11
- **as** _(seen as āsam)_ — to be, live, exist, be present
- **tvad** _(seen as tvam)_ — &c. See col. 2
- **idam** _(seen as ime)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **janādhipa** _(seen as janādhipāḥ)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **bhū** _(seen as bhaviṣyāmaḥ)_ — Bavati (rarely Ā. °te
- **sarva** _(seen as sarve)_ — whole, entire, all, every ( m. sg. ‘every one’
- **atas** _(seen as atas)_ — _(no MW gloss; not in dictionary)_
- **param** _(seen as param)_ — far, distant, remote (in space), opposite, ulterior, farther than, beyond, on the other or farther…


## BG 2.41

_vyavasāyātmikā buddhir ekeha kuru-nandana | bahu-śākhā hy anantāś ca buddhayo 'vyavasāyinām_


**Śaṅkara/advaita reading (so you know what the verse says):**
> In this path of the highest good (śreyas), O Kuru's joy, there is one and only one buddhi (discernment) — the vyavasāyātmikā (resolute, of the nature of certainty) — and it is precisely that single discernment born of right pramāṇa (valid means of knowledge) which refutes and overrides every contrary branch-proliferation of the mind. The discernments of the avyavasāyin (the irresolute, the one lacking discriminative certainty) are by contrast bahushākhā (many-branched) and anantā (endless), and it is through the unchecked spread of those branches that saṃsāra (the cycle of conditioned existenc…


**Words the parser found:**

- **vyavasāya** _(seen as vyavasāya)_ — _(no MW gloss; not in dictionary)_
- **ātmaka** _(seen as ātmikā)_ — _(no MW gloss; not in dictionary)_
- **buddhi** _(seen as buddhiḥ)_ — _(no MW gloss; not in dictionary)_
- **eka** _(seen as ekā)_ — alone, solitary, single, happening only once, that one only (frequently ifc
- **iha** _(seen as iha)_ — _(no MW gloss; not in dictionary)_
- **kuru** _(seen as kuru)_ — Comm. on ChUp
- **nandana** _(seen as nandana)_ — rejoicing, gladdening ( °daka )
- **bahu** _(seen as bahu)_ — _(no MW gloss; not in dictionary)_
- **śākhā** _(seen as śākhāḥ)_ — _(no MW gloss; not in dictionary)_
- **hi** _(seen as hi)_ — cl. 5. P. ( Dhātup. xxvii, 11 ) hinoti ( Ved. also hinute , hinvati and hinvati , °te
- **ananta** _(seen as anantāḥ)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **avyavasāyin** _(seen as avyavasāyinām)_ — _(no MW gloss; not in dictionary)_


## BG 3.17

_yas tv ātma-ratir eva syād ātma-tṛptaś ca mānavaḥ | ātmany eva ca saṃtuṣṭas tasya kāryaṃ na vidyate_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The one established in ātma-jñāna (self-knowledge) finds rati (delight) nowhere except in the ātman itself — not in the objects of the senses — and is tṛpta (satiated) by the ātman alone, not by food or taste or external pleasure. Such a sannyāsin who is santushta (fully content) in the ātman alone, having relinquished all thirst for external things, has no kartavya (duty to perform) whatsoever — for the very definition of remaining duty presupposes an unsatisfied want, and in the ātmavit (knower of Self) no such want remains.


**Words the parser found:**

- **yad** _(seen as yaḥ)_ — _(no MW gloss; not in dictionary)_
- **tu** _(seen as tu)_ — to have authority, be strong, i, 94, 2 ( pf. tUtAva Naigh. iv, 1
- **ātman** _(seen as ātma)_ — the breath
- **rati** _(seen as ratiḥ)_ — _(no MW gloss; not in dictionary)_
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **as** _(seen as syāt)_ — to be, live, exist, be present
- **tṛp** _(seen as tṛptaḥ)_ — to satiate, satisfy, refresh, gladden
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **mānava** _(seen as mānavaḥ)_ — descended from or belonging to man or Manu , human
- **saṃtuṣ** _(seen as saṃtuṣṭaḥ)_ — _(no MW gloss; not in dictionary)_
- **tad** _(seen as tasya)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **kārya** _(seen as kāryam)_ — to be caused to do, Naiṣ
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **vid** _(seen as vidyate)_ — vetti ( vidmahe , Br


## BG 3.22

_yady atra te loka-saṃgraha-kartavyatāyāṃ vipratipattis tarhi māṃ kiṃ na paśyasi ? na me pārthāsti kartavyaṃ triṣu lokeṣu kiṃcana | nānavāptam avāptavyaṃ vartaiva ca karmaṇi_


**Śaṅkara/advaita reading (so you know what the verse says):**
> For Me, O Pārtha, there is nothing whatsoever that must be done in any of the three worlds (tri-loka), nor is there anything unattained that remains to be attained — and yet I remain active in action (karman). Śaṅkara reads this as Kṛṣṇa establishing the foundational distinction between the knower (jñānin) who acts without kartṛtva-abhimāna (the conceit of agency) and the ajñānin bound by kartā-bhāva. The paradox is deliberately instructive: perfect jñāna does not terminate action; it terminates the sense of ownership over action.


**Words the parser found:**

- **yadi** _(seen as yadi)_ — if, in case that, In the earlier language yadi may be joined with Indic. Subj. or Leṭ Pot. , or…
- **atra** _(seen as atra)_ — _(no MW gloss; not in dictionary)_
- **tvad** _(seen as te)_ — &c. See col. 2
- **loka** _(seen as loka)_ — the inhabitants of the world, mankind, folk, people (sometimes opp. to ‘king’)
- **saṃgraha** _(seen as saṃgraha)_ — agglomeration (= saMyoga , q.v. ), MW
- **kṛ** _(seen as kartavya)_ — cl. 2. P. 2. sg. karzi du. kfTas pl. kfTa
- **tā** _(seen as tāyām)_ — _(no MW gloss; not in dictionary)_
- **vipratipatti** _(seen as vipratipattiḥ)_ — _(no MW gloss; not in dictionary)_
- **tarhi** _(seen as tarhi)_ — at that time, then, at that moment, in that case (correlative of yad
- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **kim** _(seen as kim)_ — kim — uta , or kim — uta-vA or kim — aTavA — uta , whether—or—or, R
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **dṛś** _(seen as paśyasi)_ — _(no MW gloss; not in dictionary)_
- **pārtha** _(seen as pārtha)_ — _(no MW gloss; not in dictionary)_
- **as** _(seen as asti)_ — to be, live, exist, be present
- **tri** _(seen as triṣu)_ — _(no MW gloss; not in dictionary)_
- **kaścana** _(seen as kiṃcana)_ — _(no MW gloss; not in dictionary)_
- **anavāpta** _(seen as anavāptam)_ — _(no MW gloss; not in dictionary)_
- **avāp** _(seen as avāptavyam)_ — to reach, attain, obtain, gain, get, Up
- **vṛt** _(seen as vartā)_ — surrounding, enclosing, obstructing (see arRo- and nadI-vft )
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **karman** _(seen as karmaṇi)_ — the object (it stands either in the acc


## BG 3.23

_yadi hy ahaṃ na varteyaṃ jātu karmaṇy atandritaḥ | mama vartmānuvartante manuṣyāḥ pārtha sarvaśaḥ_


**Words the parser found:**

- **yadi** _(seen as yadi)_ — if, in case that, In the earlier language yadi may be joined with Indic. Subj. or Leṭ Pot. , or…
- **hi** _(seen as hi)_ — cl. 5. P. ( Dhātup. xxvii, 11 ) hinoti ( Ved. also hinute , hinvati and hinvati , °te
- **mad** _(seen as aham)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **vṛt** _(seen as varteyam)_ — surrounding, enclosing, obstructing (see arRo- and nadI-vft )
- **jātu** _(seen as jātu)_ — at all, ever, x, 27, 11
- **karman** _(seen as karmaṇi)_ — the object (it stands either in the acc
- **atandrita** _(seen as atandritaḥ)_ — _(no MW gloss; not in dictionary)_
- **vartman** _(seen as vartma)_ — _(no MW gloss; not in dictionary)_
- **anuvṛt** _(seen as anuvartante)_ — _(no MW gloss; not in dictionary)_
- **manuṣya** _(seen as manuṣyāḥ)_ — _(no MW gloss; not in dictionary)_
- **pārtha** _(seen as pārtha)_ — _(no MW gloss; not in dictionary)_
- **sarvaśas** _(seen as sarvaśas)_ — _(no MW gloss; not in dictionary)_


## BG 4.14

_na māṃ karmāṇi limpanti na me karma-phale spṛhā | iti māṃ yo 'bhijānāti karmabhir na sa badhyate_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Actions do not stain Me because the sense of being a doer — the ego-root that makes karma adhere — is wholly absent. One who knows Me as the inner Self (ātman), free from the claim 'I act' and free from craving for any fruit, is likewise unbound: his actions no longer seed a body or a rebirth.


**Words the parser found:**

- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **karman** _(seen as karmāṇi)_ — the object (it stands either in the acc
- **lip** _(seen as limpanti)_ — cl. 6. 1. P. Ā. ( Dhātup. xxviii, 139 ) limpati , °te ( pf. lilepa , Br. &c
- **phala** _(seen as phale)_ — fruit ( of trees)
- **spṛhā** _(seen as spṛhā)_ — eager desire, desire, covetousness, envy, longing for, pleasure or delight in ( dat. , gen. loc. ,…
- **iti** _(seen as iti)_ — See √ i above
- **yad** _(seen as yaḥ)_ — _(no MW gloss; not in dictionary)_
- **abhijñā** _(seen as abhijānāti)_ — _(no MW gloss; not in dictionary)_
- **tad** _(seen as sa)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **bandh** _(seen as badhyate)_ — _(no MW gloss; not in dictionary)_


## BG 4.15

_evaṃ jñātvā kṛtaṃ karma pūrvair api mumukṣubhiḥ | kuru karmaiva tasmāt tvaṃ pūrvaiḥ pūrvataraṃ kṛtam_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Knowing thus — that ātman is the non-doer and karma (action) leaves no stain on it — the ancient seekers of liberation (mumukṣu) performed their prescribed duties. Therefore act, Arjuna: not silence, not renunciation. If you lack self-knowledge, act to purify the mind (ātma-śuddhi); if you possess it, act for the cohesion of the world (loka-saṃgraha), as Janaka and the ancients did long before this age.


**Words the parser found:**

- **evam** _(seen as evam)_ — _(no MW gloss; not in dictionary)_
- **jñā** _(seen as jñātvā)_ — to know, have knowledge, become acquainted with ( acc
- **kṛ** _(seen as kṛtam)_ — cl. 2. P. 2. sg. karzi du. kfTas pl. kfTa
- **karman** _(seen as karma)_ — the object (it stands either in the acc
- **pūrva** _(seen as pūrvaiḥ)_ — being before or in front, fore, first
- **api** _(seen as api)_ — and, also, moreover, besides, assuredly, surely
- **mumukṣu** _(seen as mumukṣubhiḥ)_ — _(no MW gloss; not in dictionary)_
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **tasmāt** _(seen as tasmāt)_ — from that, on that account, therefore (correlative of yad , yasmAt ), AV
- **tvad** _(seen as tvam)_ — &c. See col. 2
- **pūrvatara** _(seen as pūrvataram)_ — _(no MW gloss; not in dictionary)_


## BG 4.40

_ajñaś cāśraddadhānaś ca saṃśayātmā vinaśyati | nāyaṃ loko 'sti na paro na sukhaṃ saṃśayātmanaḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The one without ātma-jñāna (self-knowledge) and without śraddhā (faith) in the words of guru and śāstra is already diminished; but the saṃśayātmā (one whose very self is doubt) is the most ruined of all, for he is the most sinful (pāpiṣṭha). For him neither this ordinary world exists — he cannot accomplish even worldly aims — nor does the higher world, nor any sukha (happiness), because doubt arises even there. Therefore saṃśaya must not be entertained: it is the root destruction.


**Words the parser found:**

- **ajña** _(seen as ajñaḥ)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **aśraddadhāna** _(seen as aśraddadhānaḥ)_ — _(no MW gloss; not in dictionary)_
- **saṃśaya** _(seen as saṃśaya)_ — _(no MW gloss; not in dictionary)_
- **ātman** _(seen as ātmā)_ — the breath
- **vinaś** _(seen as vinaśyati)_ — _(no MW gloss; not in dictionary)_
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **idam** _(seen as ayam)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **loka** _(seen as lokaḥ)_ — the inhabitants of the world, mankind, folk, people (sometimes opp. to ‘king’)
- **as** _(seen as asti)_ — to be, live, exist, be present
- **para** _(seen as paraḥ)_ — far, distant, remote (in space), opposite, ulterior, farther than, beyond, on the other or farther…
- **sukha** _(seen as sukham)_ — running swiftly or easily (only applied to cars or chariots, superl. suKa-tama ), easy


## BG 5.10

_brahmaṇy ādhāya karmāṇi saṅgaṃ tyaktvā karoti yaḥ | lipyate na sa pāpena padma-patram ivāmbhasā_


**Śaṅkara/advaita reading (so you know what the verse says):**
> He who deposits all actions in Brahman — that is, in Īśvara — as a servant deposits his labor entirely in his master, and then performs them bereft of attachment even to liberation (mokṣa) as fruit, is untouched by sin, as a lotus leaf (padma-patra) is untouched by water. The sole fruit of such action is sattva-śuddhi (purification of the inner organ), which is merely preparatory — it does not itself produce mokṣa. For Śaṅkara the ādāna (deposit) in Brahman is the decisive move: it relocates doership from the jīva to Īśvara, temporarily, until the discriminative recognition that the jīva never…


**Words the parser found:**

- **brahman** _(seen as brahmaṇi)_ — pious effusion or utterance, outpouring of the heart in worshipping the gods, prayer
- **ādhā** _(seen as ādhāya)_ — _(no MW gloss; not in dictionary)_
- **karman** _(seen as karmāṇi)_ — the object (it stands either in the acc
- **saṅga** _(seen as saṅgam)_ — _(no MW gloss; not in dictionary)_
- **tyaj** _(seen as tyaktvā)_ — to leave, abandon, quit, x, 71, 6
- **kṛ** _(seen as karoti)_ — cl. 2. P. 2. sg. karzi du. kfTas pl. kfTa
- **yad** _(seen as yaḥ)_ — _(no MW gloss; not in dictionary)_
- **lip** _(seen as lipyate)_ — cl. 6. 1. P. Ā. ( Dhātup. xxviii, 139 ) limpati , °te ( pf. lilepa , Br. &c
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **tad** _(seen as sa)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **pāpa** _(seen as pāpena)_ — ( ŚBr. xiv  , also pApa ) n. bad, vicious, wicked, evil, wretched, vile, low
- **padma** _(seen as padma)_ — a lotus ( the flower of the lotus-plant Nelumbium Speciosum which closes towards evening
- **pattra** _(seen as patram)_ — (sometimes spelt patra ) the wing of a bird, pinion, feather, VS
- **iva** _(seen as iva)_ — _(no MW gloss; not in dictionary)_
- **ambhas** _(seen as ambhasā)_ — ( as ) sg. the number ‘four’


## BG 5.21

_bāhya-sparśeṣv asaktātmā vindaty ātmani yat sukham | sa brahma-yoga-yuktātmā sukham akṣayam aśnute_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The one whose inner organ (antahkarana) is unattached to external sense-objects — sound and the rest, the bāhya-sparśas (outer touches) — discovers through that very non-attachment the joy that belongs to the Self alone. Śaṅkara insists this ātma-sukha is not a new acquisition: it is the Self's own nature, veiled only by craving. United through brahma-yoga (samādhi on Brahman), the yogin tastes inexhaustible joy — not because Brahman gives something extra, but because the obstruction of sense-pleasure has been removed. Therefore, one who desires akṣaya-sukha (imperishable joy) must withdraw th…


**Words the parser found:**

- **bāhya** _(seen as bāhya)_ — being outside (a door, house, &c.), situated without ( abl. or comp. ), outer, exterior ( acc. with…
- **sparśa** _(seen as sparśeṣu)_ — _(no MW gloss; not in dictionary)_
- **asakta** _(seen as asakta)_ — _(no MW gloss; not in dictionary)_
- **ātman** _(seen as ātmā)_ — the breath
- **vid** _(seen as vindati)_ — vetti ( vidmahe , Br
- **yad** _(seen as yat)_ — _(no MW gloss; not in dictionary)_
- **sukha** _(seen as sukham)_ — running swiftly or easily (only applied to cars or chariots, superl. suKa-tama ), easy
- **tad** _(seen as sa)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **brahman** _(seen as brahma)_ — pious effusion or utterance, outpouring of the heart in worshipping the gods, prayer
- **yoga** _(seen as yoga)_ — the act of yoking, joining, attaching, harnessing, putting to (of horses)
- **yuj** _(seen as yukta)_ — cl. 7. P. Ā. ( Dhātup. xxix, 7 ) yunakti , yuNkte ( ep. also yuYjati , °te
- **akṣaya** _(seen as akṣayam)_ — _(no MW gloss; not in dictionary)_
- **aś** _(seen as aśnute)_ — _(no MW gloss; not in dictionary)_


## BG 5.26

_kāma-krodha-viyuktānāṃ yatīnāṃ yata-cetasām | abhito brahma-nirvāṇaṃ vartate viditātmanām_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Those wandering ascetics (yatīnāḥ) who have fully expelled desire and anger, whose inner organ (antaḥkaraṇa) is mastered, and who are established in true seeing (samyag-darśana) already possess liberation — Brahman-cessation (brahma-nirvāṇa) obtains for them on both sides, in life and in death. Śaṅkara is insistent: this is not a future attainment but a present fact, because the ātman was never un-known, only misapprehended. The verse serves as sūtra-stitching toward the inner support of right-seeing, namely dhyāna-yoga, which the following verses will elaborate.


**Words the parser found:**

- **kāma** _(seen as kāma)_ — desirous of, desiring, having a desire or intention ( go-k ° , Darma-k °
- **krodha** _(seen as krodha)_ — the breast, chest, bosom (of men and animals), AV
- **viyuj** _(seen as viyuktānām)_ — to forsake, abandon ( acc. ), Kir
- **yati** _(seen as yatīnām)_ — a disposer, vii, 13, 1 ( Sāy. ‘a giver’)
- **yam** _(seen as yata)_ — yacCati ( Ved. also °te , and Ved. ep. yamati , °te
- **cetas** _(seen as cetasām)_ — consciousness, intelligence, thinking soul, heart, mind, VS. xxxiv, 3
- **abhitas** _(seen as abhitas)_ — on both sides, ŚBr. &c
- **brahman** _(seen as brahma)_ — pious effusion or utterance, outpouring of the heart in worshipping the gods, prayer
- **nirvāṇa** _(seen as nirvāṇam)_ — _(no MW gloss; not in dictionary)_
- **vṛt** _(seen as vartate)_ — surrounding, enclosing, obstructing (see arRo- and nadI-vft )
- **vid** _(seen as vidita)_ — vetti ( vidmahe , Br
- **ātman** _(seen as ātmanām)_ — the breath


## BG 6.10

_yogī yuñjīta satatam ātmānaṃ rahasi sthitaḥ | ekākī yata-cittātmā nirāśīr aparigrahaḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The meditator (yogī) must continuously apply the inner organ (antaḥkaraṇa) in solitude — a cave or mountaintop — having renounced all association, all craving (vīta-tṛṣṇā), and every last possession (parigraha-rahita). Śaṅkara insists the qualifiers 'solitary' and 'withdrawn' together signal complete renunciation (saṃnyāsa), not merely physical aloneness. Without that renunciation, the so-called yoga is still ego-driven motion, not the stillness that opens the way to non-dual knowledge (jñāna).


**Words the parser found:**

- **yogin** _(seen as yogī)_ — or contemplative saint, devotee, ascetic, MaitrUp
- **yuj** _(seen as yuñjīta)_ — cl. 7. P. Ā. ( Dhātup. xxix, 7 ) yunakti , yuNkte ( ep. also yuYjati , °te
- **satatam** _(seen as satatam)_ — constant, perpetual, continual, uninterrupted (only in comp. and am ind. ‘constantly, always, ever’
- **ātman** _(seen as ātmānam)_ — the breath
- **rahas** _(seen as rahasi)_ — swiftness, speed, velocity, BhP
- **sthā** _(seen as sthitaḥ)_ — _(no MW gloss; not in dictionary)_
- **ekākin** _(seen as ekākī)_ — alone, solitary, AV. xix, 56, 1
- **yam** _(seen as yata)_ — yacCati ( Ved. also °te , and Ved. ep. yamati , °te
- **citta** _(seen as citta)_ — the heart, mind, TS. i
- **nirāśī** _(seen as nirāśīḥ)_ — _(no MW gloss; not in dictionary)_
- **aparigraha** _(seen as aparigrahaḥ)_ — _(no MW gloss; not in dictionary)_


## BG 6.14

_praśāntātmā vigata-bhīr brahmacāri-vrate sthitaḥ | manaḥ saṃyamya mac-citto yukta āsīta mat-paraḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The meditator whose inner organ (antaḥkaraṇa) is wholly calmed—whose fear has dissolved and who keeps the brahmacarya (celibacy-and-discipline) vow—should draw the mind's movements inward and remain seated with consciousness fixed on the Supreme Lord. Śaṅkara sharply distinguishes the rāgin whose mind follows a woman yet whose deepest allegiance is to some king or deity: this sādhaka's allegiance and awareness rest in Kṛṣṇa alone, mat-para (having Me as the highest). That non-dual absorption, not devotional sentiment, is the operative reality here.


**Words the parser found:**

- **praśam** _(seen as praśānta)_ — _(no MW gloss; not in dictionary)_
- **ātman** _(seen as ātmā)_ — the breath
- **vigam** _(seen as vigata)_ — _(no MW gloss; not in dictionary)_
- **bhī** _(seen as bhīḥ)_ — biBeti ( du. biBItas or biBitas Pot. biBIyAt or biBiyAt , Pāṇ. vi, 4, 115
- **brahmacārin** _(seen as brahmacāri)_ — or who practises chastity, a young Br° before marriage (in the first period of his life), AV
- **vrata** _(seen as vrate)_ — will, command, law, ordinance, rule
- **sthā** _(seen as sthitaḥ)_ — _(no MW gloss; not in dictionary)_
- **manas** _(seen as manaḥ)_ — _(no MW gloss; not in dictionary)_
- **saṃyam** _(seen as saṃyamya)_ — _(no MW gloss; not in dictionary)_
- **mad** _(seen as mad)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **citta** _(seen as cittaḥ)_ — the heart, mind, TS. i
- **yuj** _(seen as yuktaḥ)_ — cl. 7. P. Ā. ( Dhātup. xxix, 7 ) yunakti , yuNkte ( ep. also yuYjati , °te
- **ās** _(seen as āsīta)_ — Ah! Oh! &c
- **para** _(seen as paraḥ)_ — far, distant, remote (in space), opposite, ulterior, farther than, beyond, on the other or farther…


## BG 6.21

_sukham ātyantikaṃ yat tad buddhi-grāhyam atīndriyam | vetti yatra na caivāyaṃ sthitaś calati tattvataḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> That happiness which is absolute — without end or gradation — is grasped by the intellect (buddhi) alone, operating free of the sense organs; it is beyond sense-contact entirely. The wise one who abides in that state does not merely experience it: he knows it as his own nature, and having so known, does not fall away from that essential form (tattva). Śaṅkara is precise: the modifier 'ātyantikaṃ' means literally 'extreme-continuous,' synonymous with ananta — it is not an intensified pleasure but the abolition of the pleasure-pain axis altogether.


**Words the parser found:**

- **sukha** _(seen as sukham)_ — running swiftly or easily (only applied to cars or chariots, superl. suKa-tama ), easy
- **ātyantika** _(seen as ātyantikam)_ — _(no MW gloss; not in dictionary)_
- **yad** _(seen as yat)_ — _(no MW gloss; not in dictionary)_
- **tad** _(seen as tat)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **buddhi** _(seen as buddhi)_ — _(no MW gloss; not in dictionary)_
- **grah** _(seen as grāhyam)_ — to seize, take (by the hand, pARO or kare , exceptionally pARim (double acc. ), i, 125, 1
- **atīndriya** _(seen as atīndriyam)_ — senses
- **vid** _(seen as vetti)_ — vetti ( vidmahe , Br
- **yatra** _(seen as yatra)_ — in or to which place, where, wherein, wherever, whither, ( yatra yatra , ‘wherever’, ‘whithersoever’
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **idam** _(seen as ayam)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **sthā** _(seen as sthitaḥ)_ — _(no MW gloss; not in dictionary)_
- **cal** _(seen as calati)_ — cl. 1. °lati (metrically also Ā. °te
- **tattva** _(seen as tattvataḥ)_ — a true principle (in Sāṃkhya phil. 25 in number, viz. a-vyakta , budDi , ahaM-kAra , the 5…


## BG 7.16

_catur-vidhā bhajante māṃ janāḥ sukṛtino 'rjuna | ārto jijñāsur arthārthī jñānī ca bharatarṣabha_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Four kinds of meritorious ones (sukṛtinaḥ) approach Me — the distressed (ārta), the inquisitive (jijñāsu), the wealth-seeker (arthārthī), and the knower (jñānī). Śaṅkara specifies the ārta as one overwhelmed by thieves, tigers, disease and such calamities, and the arthārthī as one desiring wealth (dhana-kāma) — both still entangled in conditional aims. The jñānī alone knows the true nature (tattva) of Viṣṇu and therefore stands apart; the other three are preparatory grades on the path toward jñāna, which alone dissolves the illusion of the individual self.


**Words the parser found:**

- **catur** _(seen as catur)_ — _(no MW gloss; not in dictionary)_
- **vidha** _(seen as vidhāḥ)_ — _(no MW gloss; not in dictionary)_
- **bhaj** _(seen as bhajante)_ — Bajati , °te (2. sg. as Impv. Bakzi
- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **jana** _(seen as janāḥ)_ — creature, living being, man, person, race ( paYca janAs , ‘the five races’ = p ° kfzwayas , iii  ,…
- **sukṛtin** _(seen as sukṛtinaḥ)_ — _(no MW gloss; not in dictionary)_
- **arjuna** _(seen as arjuna)_ — white, clear (the colour of the day, vi, 9, 1
- **ārta** _(seen as ārtaḥ)_ — fallen into (misfortune), struck by calamity, afflicted, pained, disturbed
- **jijñāsu** _(seen as jijñāsuḥ)_ — _(no MW gloss; not in dictionary)_
- **artha** _(seen as artha)_ — _(no MW gloss; not in dictionary)_
- **arthin** _(seen as arthī)_ — _(no MW gloss; not in dictionary)_
- **jñānin** _(seen as jñānī)_ — knowing the higher knowledge or knowledge of spirit ( Kathās. lxxix  ), xii, 103
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **bharata** _(seen as bharata)_ — _(no MW gloss; not in dictionary)_
- **ṛṣabha** _(seen as ṛṣabha)_ — _(no MW gloss; not in dictionary)_


## BG 7.24

_avyaktaṃ vyaktim āpannaṃ manyante mām abuddhayaḥ | paraṃ bhāvam ajānanto mamāvyayam anuttamam_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The undiscerning (abuddhayaḥ, 'those without viveka') mistake me — the eternally established Īśvara — for one who has merely moved from the unmanifest (avyaktam, 'the unillumined') into a manifest personal form (vyaktim āpannam). They do so because they fail to know my supreme nature (paraṃ bhāvam), which is the very form of the Paramātman. That nature of mine is without diminution (avyayam, 'without expenditure') and admits no superior (anuttamam) — yet viḍambana (the folly of confusing nirguṇa Brahman with a finite form) blinds them to this.


**Words the parser found:**

- **avyakta** _(seen as avyaktam)_ — unknown as quantity or number
- **vyakti** _(seen as vyaktim)_ — gender, Pāṇ. i, 2, 51
- **āpad** _(seen as āpannam)_ — to come, walk near, approach, BhP
- **man** _(seen as manyante)_ — manute , manyate ( ep. also °ti
- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **abuddhi** _(seen as abuddhayaḥ)_ — _(no MW gloss; not in dictionary)_
- **para** _(seen as param)_ — far, distant, remote (in space), opposite, ulterior, farther than, beyond, on the other or farther…
- **bhāva** _(seen as bhāvam)_ — becoming, being, existing, occurring, appearance, ŚvetUp
- **a** _(seen as a)_ — _(no MW gloss; not in dictionary)_
- **jñā** _(seen as jānantaḥ)_ — to know, have knowledge, become acquainted with ( acc
- **avyaya** _(seen as avyayam)_ — made of sheep's skin (as the woollen Soma strainer)
- **anuttama** _(seen as anuttamam)_ — not used in the uttama , or first person


## BG 7.27

_icchā-dveṣa-samutthena dvandva-mohena bhārata | sarva-bhūtāni saṃmohaṃ sarge yānti parantapa_


**Śaṅkara/advaita reading (so you know what the verse says):**
> All beings enter deep delusion (saṃmoha) at birth — not by accident but by the structural action of dvandva-moha (the delusion born of the pairs), which is itself produced by icchā (desire) and dveṣa (aversion) that have possessed the buddhi (intellect). Śaṅkara is precise: when icchā and dveṣa gain ground through contact with pleasure, pain, and their causes, they generate moha that blocks the very arising of paramārtha-ātma-tattva-viṣaya-jñāna (knowledge of the supreme Self). Because all beings arise already in the grip of this moha, they do not know the ātman as their true nature and theref…


**Words the parser found:**

- **icchā** _(seen as icchā)_ — a question or problem
- **dveṣa** _(seen as dveṣa)_ — _(no MW gloss; not in dictionary)_
- **samuttha** _(seen as samutthena)_ — _(no MW gloss; not in dictionary)_
- **dvaṃdva** _(seen as dvandva)_ — pair, couple, male and female, TS
- **moha** _(seen as mohena)_ — loss of consciousness, bewilderment, perplexity, distraction, infatuation, delusion, error, folly,…
- **bhārata** _(seen as bhārata)_ — _(no MW gloss; not in dictionary)_
- **sarva** _(seen as sarva)_ — whole, entire, all, every ( m. sg. ‘every one’
- **bhūta** _(seen as bhūtāni)_ — being or being like anything, consisting of, mixed or joined with, Prāt
- **sammoha** _(seen as saṃmoham)_ — a partic. conjunction of planets, VarBṛS
- **sarga** _(seen as sarge)_ — letting go, discharging, voiding (as excrement)
- **yā** _(seen as yānti)_ — a goer or mover
- **paraṃtapa** _(seen as parantapa)_ — _(no MW gloss; not in dictionary)_


## BG 8.1

_kiṃ tad brahma kim adhyātmaṃ kiṃ karma puruṣottama | adhibhūtaṃ ca kiṃ proktam adhidaivaṃ kim ucyate_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Arjuna asks: What is that Brahman? What is adhyātma (the self as inner ground)? What is karma, O Puruṣottama? Śaṅkara reads these as the seven technical seeds sown at the end of Chapter 7 — the unanswered pratiśruti (implicit promise) that compels Chapter 8. The seven terms are not idle curiosity; they are the epistemological preconditions for the inquiry into liberation from birth and death (jarā-maraṇa-mokṣa), and Arjuna now demands each be specified so that jñāna can proceed without ambiguity.


**Words the parser found:**

- **ka** _(seen as kim)_ — ka is often connected with a demonstrative pron. ( ko 'yam AyAti , who comes here?) or with the…
- **tad** _(seen as tat)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **brahman** _(seen as brahma)_ — pious effusion or utterance, outpouring of the heart in worshipping the gods, prayer
- **adhyātma** _(seen as adhyātmam)_ — _(no MW gloss; not in dictionary)_
- **karman** _(seen as karma)_ — the object (it stands either in the acc
- **puruṣottama** _(seen as puruṣottama)_ — _(no MW gloss; not in dictionary)_
- **adhibhūta** _(seen as adhibhūtam)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **pravac** _(seen as proktam)_ — _(no MW gloss; not in dictionary)_
- **adhidaiva** _(seen as adhidaivam)_ — _(no MW gloss; not in dictionary)_
- **vac** _(seen as ucyate)_ — vakti (occurs only in sg. vacmi , vakzi , vakti , and Impv. vaktu


## BG 8.15

_mām upetya punar-janma duḥkhālayam aśāśvatam | nāpnuvanti mahātmānaḥ saṃsiddhiṃ paramāṃ gatāḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Reaching Me — the Lord — and attaining My very nature (mad-bhāva), the great ones no longer return to rebirth, which is a receptacle (ālaya) for all three types of suffering (ādhyātmika and the rest) and whose own form is never stable. They have arrived at that highest accomplishment called liberation (mokṣa-ākhyā saṃsiddhi). Those who do not reach Me, Śaṅkara clarifies, rotate back into saṃsāra.


**Words the parser found:**

- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **upe** _(seen as upetya)_ — P. -Eti , to go or come or step near, approach, betake one's self to, arrive at, meet with, turn…
- **punar** _(seen as punar)_ — _(no MW gloss; not in dictionary)_
- **janman** _(seen as janma)_ — N. of the 1st lunar mansion, civ
- **duḥkha** _(seen as duḥkha)_ — uneasy, uncomfortable, unpleasant, difficult, R
- **ālaya** _(seen as ālayam)_ — _(no MW gloss; not in dictionary)_
- **aśāśvata** _(seen as aśāśvatam)_ — _(no MW gloss; not in dictionary)_
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **āp** _(seen as āpnuvanti)_ — to reach, overtake, meet with, fall upon
- **mahātman** _(seen as mahātmānaḥ)_ — ‘high-souled’, magnanimous, having a gr° or noble nature, high-minded, noble
- **saṃsiddhi** _(seen as saṃsiddhim)_ — _(no MW gloss; not in dictionary)_
- **parama** _(seen as paramām)_ — most distant, remotest, extreme, last
- **gam** _(seen as gatāḥ)_ — : cl. 3. P. jaganti ( Naigh. ii, 14


## BG 8.25

_dhūmo rātris tathā kṛṣṇaḥ ṣaṇ-māsā dakṣiṇāyanam | tatra cāndramasaṃ jyotir yogī prāpya nivartate_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Śaṅkara reads each term — dhūma (smoke), rātri (night), kṛṣṇa (dark fortnight), and the six months of dakṣiṇāyana — not as literal cosmological stations but as the presiding deities (abhimāni-devatā) of those phenomena, who conduct the departing soul along the pitṛyāna. The karmī who performs iṣṭa (Vedic rite) and pūrta (charitable work) reaches the cāndramasa-jyotis, enjoys the fruit of merit, and upon its exhaustion returns (nivartate) to rebirth. For Śaṅkara the contrast with 8.24 is stark: the jñānī who traverses the arcirādi-mārga does not return; the sakāma-karmī always does — hence the …


**Words the parser found:**

- **dhūma** _(seen as dhūmaḥ)_ — _(no MW gloss; not in dictionary)_
- **rātri** _(seen as rātriḥ)_ — rAtrI ( prob. ‘bestower’, fr. √ rA
- **tathā** _(seen as tathā)_ — _(no MW gloss; not in dictionary)_
- **kṛṣṇa** _(seen as kṛṣṇaḥ)_ — _(no MW gloss; not in dictionary)_
- **ṣaṣ** _(seen as ṣaṭ)_ — cl. 1. P. ( Dhātup. xvii, 77 ) SaSati (only pr. p. SaSat , Kir. xv, 5  ), to leap, bound, dance
- **māsa** _(seen as māsāḥ)_ — the moon (see pUrRa-m ° )
- **dakṣiṇāyana** _(seen as dakṣiṇāyanam)_ — _(no MW gloss; not in dictionary)_
- **tatra** _(seen as tatra)_ — ( ta-tra , correlative of ya-tra
- **cāndramasa** _(seen as cāndramasam)_ — lunar, relating to the moon, AV. xix, 9, 10
- **jyotis** _(seen as jyotiḥ)_ — _(no MW gloss; not in dictionary)_
- **yogin** _(seen as yogī)_ — or contemplative saint, devotee, ascetic, MaitrUp
- **prāp** _(seen as prāpya)_ — P. Ā. prA pnoti ( irreg. Pot. prA peyam ), to attain to
- **nivṛt** _(seen as nivartate)_ — to ( acc. with or without prati , or dat. )


## BG 9.4

_mayā tatam idaṃ sarvaṃ jagad avyakta-mūrtinā | mat-sthāni sarva-bhūtāni na cāhaṃ teṣv avasthitaḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> By My transcendent nature — avyakta-mūrti (unmanifest form), beyond all sense-contact — this entire cosmos is pervaded, as space pervades a vessel without being the vessel. All beings from Brahmā down to a blade of grass rest in Me as their innermost ātman (self), for nothing can function in transactional reality that is self-less. Yet I do not abide in them the way a tangible object rests in a container — being asaṃsargi (unattached, contact-free), I am in truth even more interior to space than space itself; the relation is not ādheyatā (locative containment) but ātmatā (being the very self).


**Words the parser found:**

- **mad** _(seen as mayā)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **tan** _(seen as tatam)_ — cl. 4. °nyati ( aor. 2. sg. tatanas ) to resound, roar, i, 38, 14
- **idam** _(seen as idam)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **sarva** _(seen as sarvam)_ — whole, entire, all, every ( m. sg. ‘every one’
- **jagant** _(seen as jagat)_ — _(no MW gloss; not in dictionary)_
- **avyakta** _(seen as avyakta)_ — unknown as quantity or number
- **mūrti** _(seen as mūrtinā)_ — _(no MW gloss; not in dictionary)_
- **stha** _(seen as sthāni)_ — _(no MW gloss; not in dictionary)_
- **bhūta** _(seen as bhūtāni)_ — being or being like anything, consisting of, mixed or joined with, Prāt
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **tad** _(seen as teṣu)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **avasthā** _(seen as avasthitaḥ)_ — _(no MW gloss; not in dictionary)_


## BG 9.22

_ananyāś cintayanto māṃ ye janāḥ paryupāsate | teṣāṃ nityābhiyuktānāṃ yoga-kṣemaṃ vahāmy aham_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Those who are ananyah (non-separate) — who have realized the Supreme Lord Nārāyaṇa as their very ātman and thus ceased to conceive any object of meditation apart from That — Śaṅkara distinguishes these from ordinary devotees: other bhaktas still strive for their own yogakṣema (acquisition and preservation of worldly needs), but the paramārthadarśins (seers of ultimate truth) do not seek even their own survival, being solely śaraṇāgata (surrendered) in Bhagavān. Because the jñānī is ātmaiva (verily the Self of the Lord), the Lord bears their yogakṣema without any effort on their part — not as a…


**Words the parser found:**

- **an** _(seen as an)_ — the substitute for 3. a , or a privative
- **anya** _(seen as anyāḥ)_ — _(no MW gloss; not in dictionary)_
- **cintay** _(seen as cintayantaḥ)_ — _(no MW gloss; not in dictionary)_
- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **yad** _(seen as ye)_ — _(no MW gloss; not in dictionary)_
- **jana** _(seen as janāḥ)_ — creature, living being, man, person, race ( paYca janAs , ‘the five races’ = p ° kfzwayas , iii  ,…
- **paryupās** _(seen as paryupāsate)_ — Ā. -upA ste (3. pl. -upA sate Pot. 3. sg. -upA sIta
- **tad** _(seen as teṣām)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **nitya** _(seen as nitya)_ — innate, native, iii, 13941
- **abhiyuj** _(seen as abhiyuktānām)_ — for a special purpose ( acc. ), ŚBr. : P. to put to (as horses) subsequently, ŚBr. : Ā. to summon,…
- **yoga** _(seen as yoga)_ — the act of yoking, joining, attaching, harnessing, putting to (of horses)
- **kṣema** _(seen as kṣemam)_ — _(no MW gloss; not in dictionary)_
- **vah** _(seen as vahāmi)_ — vahati , °te (in later language Ā. only mc


## BG 9.33

_kiṃ punar brāhmaṇāḥ puṇyā bhaktā rājarṣayas tathā | anityam asukhaṃ lokam imaṃ prāpya bhajasva mām_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Even those of meritorious birth — the twice-born (dvija) who are fit vessels, and the royal sages (rājarṣi) who wield both rule and renunciation — attain liberation through devotion; how much more certain, then, is that path for the qualified. Śaṅkara's gloss presses the urgency: human birth (manuṣyatva) is rare (durlabha) and momentary (kṣaṇabhaṅgura), a fleeting occasion for pursuing the supreme end (puruṣārtha), utterly devoid of inherent enjoyment (sukhavajita). The imperative 'bhajasva' is therefore not an invitation but an insistence: seize this impermanent vehicle for the only work it i…


**Words the parser found:**

- **ka** _(seen as kim)_ — ka is often connected with a demonstrative pron. ( ko 'yam AyAti , who comes here?) or with the…
- **punar** _(seen as punar)_ — _(no MW gloss; not in dictionary)_
- **brāhmaṇa** _(seen as brāhmaṇāḥ)_ — _(no MW gloss; not in dictionary)_
- **puṇya** _(seen as puṇyāḥ)_ — _(no MW gloss; not in dictionary)_
- **bhakta** _(seen as bhaktāḥ)_ — forming part of, belonging to, Pāṇ. , Sch
- **rājarṣi** _(seen as rājarṣayaḥ)_ — _(no MW gloss; not in dictionary)_
- **tathā** _(seen as tathā)_ — _(no MW gloss; not in dictionary)_
- **anitya** _(seen as anityam)_ — _(no MW gloss; not in dictionary)_
- **asukha** _(seen as asukham)_ — _(no MW gloss; not in dictionary)_
- **loka** _(seen as lokam)_ — the inhabitants of the world, mankind, folk, people (sometimes opp. to ‘king’)
- **idam** _(seen as imam)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **prāp** _(seen as prāpya)_ — P. Ā. prA pnoti ( irreg. Pot. prA peyam ), to attain to
- **bhaj** _(seen as bhajasva)_ — Bajati , °te (2. sg. as Impv. Bakzi
- **mad** _(seen as mām)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te


## BG 10.1

_bhūya eva mahā-bāho śṛṇu me paramaṃ vacaḥ | yat te 'haṃ prīyamāṇāya vakṣyāmi hita-kāmyayā_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Śrī Bhagavān said: Once more, O Mahābāhu (mighty-armed), hear My supreme word (paramam vacah), that which reveals the unsurpassable reality (niratiśaya-vastu) — for you drink it like nectar (amrita-iva). I shall declare it again out of desire for your good (hita-kāmyayā).


**Words the parser found:**

- **bhūyas** _(seen as bhūyas)_ — more, more numerous or abundant, greater, larger, mightier (also ‘much or many, very numerous or…
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **mahat** _(seen as mahā)_ — great (in space, time, quantity or degree) large, big, huge, ample, extensive, long, abundant,…
- **bāhu** _(seen as bāho)_ — ( fr. √ bah , baMh
- **śru** _(seen as śṛṇu)_ — _(no MW gloss; not in dictionary)_
- **mad** _(seen as me)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **parama** _(seen as paramam)_ — most distant, remotest, extreme, last
- **vacas** _(seen as vacaḥ)_ — speech, voice, word, ( °casAmpatiH N. of Bṛhaspati , Laghuj. )
- **yad** _(seen as yat)_ — _(no MW gloss; not in dictionary)_
- **tvad** _(seen as te)_ — &c. See col. 2
- **prī** _(seen as prīyamāṇāya)_ — prIRAti , prIRIte
- **vac** _(seen as vakṣyāmi)_ — vakti (occurs only in sg. vacmi , vakzi , vakti , and Impv. vaktu
- **hita** _(seen as hita)_ — sent, impelled, urged on, set in motion &c
- **kāmyā** _(seen as kāmyayā)_ — _(no MW gloss; not in dictionary)_


## BG 10.5

_ahiṃsā samatā tuṣṭis tapo dānaṃ yaśo 'yaśaḥ | bhavanti bhāvā bhūtānāṃ matta eva pṛthag-vidhāḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Ahiṃsā (non-injury to living beings), samatā (equanimity of mind), tuṣṭi (contentment at whatever gain suffices), tapas (bodily austerity preceded by restraint of the senses), dāna (distribution according to one's capacity), yaśas (fame arising from dharma), and ayaśas (ill-fame arising from adharma) — these manifold dispositions of all creatures arise from Me alone, the Īśvara, each differentiated in accordance with the creature's own past karma. Brahman, as the sole efficient cause underlying all phenomenal distinctions, generates the entire field of mental and moral qualities that the jīva …


**Words the parser found:**

- **ahiṃsā** _(seen as ahiṃsā)_ — _(no MW gloss; not in dictionary)_
- **sama** _(seen as sama)_ — any, every
- **tā** _(seen as tā)_ — _(no MW gloss; not in dictionary)_
- **tuṣṭi** _(seen as tuṣṭiḥ)_ — _(no MW gloss; not in dictionary)_
- **tapas** _(seen as tapaḥ)_ — N. of a month intervening between winter and spring, VS
- **dāna** _(seen as dānam)_ — distribution of food or of a sacrificial meal
- **yaśas** _(seen as yaśaḥ)_ — _(no MW gloss; not in dictionary)_
- **ayaśas** _(seen as ayaśaḥ)_ — _(no MW gloss; not in dictionary)_
- **bhū** _(seen as bhavanti)_ — Bavati (rarely Ā. °te
- **bhāva** _(seen as bhāvāḥ)_ — becoming, being, existing, occurring, appearance, ŚvetUp
- **bhūta** _(seen as bhūtānām)_ — being or being like anything, consisting of, mixed or joined with, Prāt
- **mad** _(seen as mattaḥ)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **pṛthak** _(seen as pṛthak)_ — _(no MW gloss; not in dictionary)_
- **vidha** _(seen as vidhāḥ)_ — _(no MW gloss; not in dictionary)_


## BG 10.25

_maharṣīṇāṃ bhṛgur ahaṃ girām asmy ekam akṣaram | yajñānāṃ japa-yajño 'smi sthāvarāṇāṃ himālayaḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Among the great seers (maharṣīṇām), I am Bhṛgu — the blazing fire of discriminative insight that reduces all apparent multiplicity to the singularity of Brahman. Among words (girām), I am the one imperishable syllable (ekam akṣaram) — Oṃkāra — for all articulated speech is modification, but Oṃ alone is the unmodified sound-form of pure Consciousness. Among sacrifices (yajñānām), I am japa-yajña, for silent repetition approaches contemplation (manana) without the duality of performer and instrument; and among the unmovings (sthāvarāṇām), I am the Himālaya — a mass so stable it serves as viveka-…


**Words the parser found:**

- **mahat** _(seen as mahā)_ — great (in space, time, quantity or degree) large, big, huge, ample, extensive, long, abundant,…
- **ṛṣi** _(seen as ṛṣīṇām)_ — _(no MW gloss; not in dictionary)_
- **bhṛgu** _(seen as bhṛguḥ)_ — N. of a mythical race of beings (closely connected with fire, which they find
- **mad** _(seen as aham)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **gir** _(seen as girām)_ — addressing, invoking, praising
- **as** _(seen as asmi)_ — to be, live, exist, be present
- **eka** _(seen as ekam)_ — alone, solitary, single, happening only once, that one only (frequently ifc
- **akṣara** _(seen as akṣaram)_ — _(no MW gloss; not in dictionary)_
- **yajña** _(seen as yajñānām)_ — N. of the reputed author of x, 130 , Anukr
- **japa** _(seen as japa)_ — muttering prayers, repeating in a murmuring tone passages from scripture or charms or names of a…
- **sthāvara** _(seen as sthāvarāṇām)_ — _(no MW gloss; not in dictionary)_
- **himālaya** _(seen as himālayaḥ)_ — _(no MW gloss; not in dictionary)_


## BG 11.6

_paśyādityān vasūn rudrān aśvinau marutas tathā | bahūny adṛṣṭa-pūrvāṇi paśyāścaryāṇi bhārata_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Behold here the twelve Ādityas, the eight Vasus, the eleven Rudras, the two Aśvins, and the forty-nine Maruts — all of whom in the ordinary world (manuṣya-loka) neither you nor any other has ever perceived. These many wonders (āścarya, remarkable because they exceed the reach of common cognition) are gathered in this single divine form (viśvarūpa). The listing is not exhaustive but indicative: the point is the inexhaustible wealth of manifest appearance that the One Brahman sustains without itself becoming many.


**Words the parser found:**

- **paś** _(seen as paśya)_ — _(no MW gloss; not in dictionary)_
- **āditya** _(seen as ādityān)_ — N. of a constellation, the seventh lunar mansion
- **vasu** _(seen as vasūn)_ — excellent, good, beneficent
- **rudra** _(seen as rudrān)_ — crying, howling, roaring, dreadful, terrific, terrible, horrible (applied to the Aśvin s, Agni ,…
- **aśvin** _(seen as aśvinau)_ — _(no MW gloss; not in dictionary)_
- **marut** _(seen as marutaḥ)_ — the storm-gods (Indra 's companions and sometimes, Ragh. xii, 101 = devAH , the gods or deities in…
- **tathā** _(seen as tathā)_ — _(no MW gloss; not in dictionary)_
- **bahu** _(seen as bahūni)_ — _(no MW gloss; not in dictionary)_
- **adṛṣṭa** _(seen as adṛṣṭa)_ — _(no MW gloss; not in dictionary)_
- **pūrva** _(seen as pūrvāṇi)_ — being before or in front, fore, first
- **āścarya** _(seen as āścaryāṇi)_ — _(no MW gloss; not in dictionary)_
- **bhārata** _(seen as bhārata)_ — _(no MW gloss; not in dictionary)_


## BG 11.19

_anādi-madhyāntam ananta-vīryam ananta-bāhuṃ śaśi-sūrya-netram | paśyāmi tvāṃ dīpta-hutāśa-vaktraṃ sva-tejasā viśvam idaṃ tapantam_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Arjuna beholds the one Reality that has no origin (ādi), no middle (madhya), no end (anta) — the very structure of time is absent in what is seen, because what is seen is not a temporal object but the substrate of time itself. The infinite power (ananta-vīrya) and infinite arms (ananta-bāhu) are not enumerable attributes added to a substance; Śaṅkara reads each compound as denying any limit external to the Whole: no boundary of potency exists, no boundary of reach exists. The moon and sun are the two eyes (śaśi-sūrya-netra); the blazing fire-face (dīpta-hutāśa-vaktra) is one more limb of this …


**Words the parser found:**

- **anādi** _(seen as anādi)_ — _(no MW gloss; not in dictionary)_
- **madhya** _(seen as madhya)_ — _(no MW gloss; not in dictionary)_
- **anta** _(seen as antam)_ — _(no MW gloss; not in dictionary)_
- **ananta** _(seen as ananta)_ — _(no MW gloss; not in dictionary)_
- **vīrya** _(seen as vīryam)_ — manliness, valour, strength, power, energy
- **bāhu** _(seen as bāhum)_ — ( fr. √ bah , baMh
- **śaśin** _(seen as śaśi)_ — _(no MW gloss; not in dictionary)_
- **sūrya** _(seen as sūrya)_ — _(no MW gloss; not in dictionary)_
- **netra** _(seen as netram)_ — leading, guiding, conducting, AV. x, 10, 22
- **dṛś** _(seen as paśyāmi)_ — _(no MW gloss; not in dictionary)_
- **tvad** _(seen as tvām)_ — &c. See col. 2
- **dīp** _(seen as dīpta)_ — to blaze, flare, shine, be luminous or illustrious, AV
- **hutāśa** _(seen as hutāśa)_ — _(no MW gloss; not in dictionary)_
- **vaktra** _(seen as vaktram)_ — the initial quantity or first term of a progression, Col
- **sva** _(seen as sva)_ — house’]
- **tejas** _(seen as tejasā)_ — the sharp edge (of a knife &c.), point or top of a flame or ray, glow, glare, splendour,…
- **viśva** _(seen as viśvam)_ — _(no MW gloss; not in dictionary)_
- **idam** _(seen as idam)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **tap** _(seen as tapantam)_ — cl. 4. Ā. °pyate , to rule, Dhātup. xxvi, 50


## BG 11.53

_nāhaṃ vedair na tapasā na dānena na cejyayā | śakya evaṃ-vidho draṣṭuṃ dṛṣṭavān asi māṃ yathā_


**Śaṅkara/advaita reading (so you know what the verse says):**
> This form cannot be seen through the four Vedas (ṛg, yajus, sāman, atharvan), nor through severe austerity (tapas) such as cāndrāyaṇa fasting, nor through gifts of cows, land, and gold (dāna), nor through ritual worship or sacrifice (ijyā). What you have seen — the viśvarūpa exactly as disclosed — is not available by any of these means. Śaṅkara's terse point: these instruments belong to the realm of karma and external action; they cannot produce direct apprehension (sākṣātkāra) of that which is beyond the empirical order. The implication, left for the next verse to name, is that knowledge alon…


**Words the parser found:**

- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **mad** _(seen as aham)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **veda** _(seen as vedaiḥ)_ — knowledge, true or sacred knowledge or lore, knowledge of ritual
- **tapas** _(seen as tapasā)_ — N. of a month intervening between winter and spring, VS
- **dāna** _(seen as dānena)_ — distribution of food or of a sacrificial meal
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **ijyā** _(seen as ijyayā)_ — _(no MW gloss; not in dictionary)_
- **śakya** _(seen as śakyaḥ)_ — _(no MW gloss; not in dictionary)_
- **evaṃvidha** _(seen as evaṃvidhaḥ)_ — _(no MW gloss; not in dictionary)_
- **dṛś** _(seen as draṣṭum)_ — _(no MW gloss; not in dictionary)_
- **as** _(seen as asi)_ — to be, live, exist, be present
- **yathā** _(seen as yathā)_ — _(no MW gloss; not in dictionary)_


## BG 12.3

_ye tv akṣaram anirdeśyam avyaktaṃ paryupāsate | sarvatra-gam acintyaṃ ca kūṭastham acalaṃ dhruvam_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Those who worship the aksara (imperishable) — which cannot be pointed to by any word because it is avyakta (unmanifest), not reachable by any means of knowledge — they meditate on it as Sankara prescribes: a sustained, unbroken flow of identical cognition, like an uninterrupted stream of oil. The aksara is sarvatra-ga (all-pervading) like space itself, acintya (unthinkable) because it lies beyond all sense-organs and hence beyond mind, kutastha (the witness-base) in the sense that it stands as the substratum beneath the kuta — the deceiving superimposition that is maya and her effects. Being u…


**Words the parser found:**

- **yad** _(seen as ye)_ — _(no MW gloss; not in dictionary)_
- **tu** _(seen as tu)_ — to have authority, be strong, i, 94, 2 ( pf. tUtAva Naigh. iv, 1
- **akṣara** _(seen as akṣaram)_ — _(no MW gloss; not in dictionary)_
- **anirdeśya** _(seen as anirdeśyam)_ — _(no MW gloss; not in dictionary)_
- **avyakta** _(seen as avyaktam)_ — unknown as quantity or number
- **paryupās** _(seen as paryupāsate)_ — Ā. -upA ste (3. pl. -upA sate Pot. 3. sg. -upA sIta
- **sarvatra** _(seen as sarvatra)_ — _(no MW gloss; not in dictionary)_
- **ga** _(seen as gam)_ — only ifc. going, moving ( yAna- , going in a carriage, iv, 120
- **acintya** _(seen as acintyam)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **kūṭastha** _(seen as kūṭastham)_ — _(no MW gloss; not in dictionary)_
- **acala** _(seen as acalam)_ — _(no MW gloss; not in dictionary)_
- **dhruva** _(seen as dhruvam)_ — _(no MW gloss; not in dictionary)_


## BG 12.17

_yo na hṛṣyati na dveṣṭi na śocati na kāṅkṣati | śubhāśubha-parityāgī bhaktimān yaḥ sa me priyaḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The one who neither exults on obtaining what is desirable (ishta-prapti) nor recoils on meeting what is undesirable (anishta-prapti), who neither grieves at separation from the beloved nor hankers after the unobtained — this is the equipoise of one whose nature (shila) it is to abandon both auspicious and inauspicious action (shubha-ashubha-parityaga). Such conduct is not a devotional sentiment but the outward mark of one in whom the root of doership has been severed by jnana. He is a bhakta only in the sense that his steady abidance in the Self is itself the supreme form of worship; the Lord …


**Words the parser found:**

- **yad** _(seen as yaḥ)_ — _(no MW gloss; not in dictionary)_
- **na** _(seen as na)_ — &c. &c. (as well in simple negation as in wishing, requesting and commanding, except in prohibition…
- **hṛṣ** _(seen as hṛṣyati)_ — _(no MW gloss; not in dictionary)_
- **dviṣ** _(seen as dveṣṭi)_ — _(no MW gloss; not in dictionary)_
- **śuc** _(seen as śocati)_ — _(no MW gloss; not in dictionary)_
- **kāṅkṣ** _(seen as kāṅkṣati)_ — _(no MW gloss; not in dictionary)_
- **śubha** _(seen as śubha)_ — _(no MW gloss; not in dictionary)_
- **aśubha** _(seen as aśubha)_ — _(no MW gloss; not in dictionary)_
- **parityāgin** _(seen as parityāgī)_ — _(no MW gloss; not in dictionary)_
- **bhaktimat** _(seen as bhaktimān)_ — _(no MW gloss; not in dictionary)_
- **tad** _(seen as sa)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **mad** _(seen as me)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **priya** _(seen as priyaḥ)_ — _(no MW gloss; not in dictionary)_


## BG 12.19

_tulya-nindā-stutir maunī saṃtuṣṭo yena kenacit | aniketaḥ sthira-matir bhaktimān me priyo naraḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The bhāṣya for this school was embedded as HTML within the advaita-bhakti payload (Śaṅkarācārya commentary recovered from that section). Śaṅkara reads 'tulya-nindā-stutiḥ' (equal in censure and praise) as the defining mark of the renunciant who has no fixed abode (anāgāra): censure and praise both produce suffering and pleasure respectively, yet to him they are identical — not through indifference alone but because the paramārtha (supreme reality) admits no such distinctions. 'Maunī' (silent one) does not mean absence of all speech but restraint of the organ of speech except where bodily subsi…


**Words the parser found:**

- **tulya** _(seen as tulya)_ — equal to, of the same kind or class or number or value, similar, comparable, like (with instr. or…
- **nindā** _(seen as nindā)_ — one of the eight worldly conditions, Dharmas. lxi
- **stuti** _(seen as stutiḥ)_ — praise, eulogy, panegyric, commendation, adulation
- **maunin** _(seen as maunī)_ — _(no MW gloss; not in dictionary)_
- **saṃtuṣ** _(seen as saṃtuṣṭaḥ)_ — _(no MW gloss; not in dictionary)_
- **yad** _(seen as yena)_ — _(no MW gloss; not in dictionary)_
- **kaścit** _(seen as kenacid)_ — _(no MW gloss; not in dictionary)_
- **aniketa** _(seen as aniketaḥ)_ — _(no MW gloss; not in dictionary)_
- **sthira** _(seen as sthira)_ — _(no MW gloss; not in dictionary)_
- **mati** _(seen as matiḥ)_ — devotion, prayer, worship, hymn, sacred utterance
- **bhaktimat** _(seen as bhaktimān)_ — _(no MW gloss; not in dictionary)_
- **mad** _(seen as me)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **priya** _(seen as priyaḥ)_ — _(no MW gloss; not in dictionary)_
- **nara** _(seen as naraḥ)_ — a man, a male, a person ( pl. men, people), TS. &c. &c


## BG 13.18

_iti kṣetraṃ tathā jñānaṃ jñeyaṃ coktaṃ samāsataḥ | mad-bhakta etad vijñāya mad-bhāvāyopapadyate_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Sankara closes the summary of kshetra (field), jnana (knowledge-means), and jneya (the knowable) by locating all three in the hrdaya (heart-intellect) of every creature — not as acquired contents but as the very light (jyotis) by which even Aditya shines. The knowable Brahman is para tamas (beyond darkness), untouched by avidya, self-luminous consciousness that is simultaneously the knower, the knowing, and the known. The mad-bhakta who penetrates this triple identity through the discipline of amanitva and its companions attains mad-bhava — not a state reached from outside, but the recognition…


**Words the parser found:**

- **iti** _(seen as iti)_ — See √ i above
- **kṣetra** _(seen as kṣetram)_ — _(no MW gloss; not in dictionary)_
- **tathā** _(seen as tathā)_ — _(no MW gloss; not in dictionary)_
- **jñāna** _(seen as jñānam)_ — the higher knowledge (derived from meditation on the one Universal Spirit), ŚāṅkhŚr. xiii
- **jñā** _(seen as jñeyam)_ — to know, have knowledge, become acquainted with ( acc
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **vac** _(seen as uktam)_ — vakti (occurs only in sg. vacmi , vakzi , vakti , and Impv. vaktu
- **samāsatas** _(seen as samāsatas)_ — _(no MW gloss; not in dictionary)_
- **mad** _(seen as mad)_ — cl. 4. P. ( Dhātup. xxvi, 99 ) mAdyati ( ep. also °te
- **bhakta** _(seen as bhaktaḥ)_ — forming part of, belonging to, Pāṇ. , Sch
- **etad** _(seen as etat)_ — this, this here, here (especially as pointing to what is nearest to the speaker, eza bARaH , this…
- **vijñā** _(seen as vijñāya)_ — : Caus. -jYapayati , or -jYApayati (rarely °te
- **bhāva** _(seen as bhāvāya)_ — becoming, being, existing, occurring, appearance, ŚvetUp
- **upapad** _(seen as upapadyate)_ — -ti , to go towards or against, attack, AV. iv, 18, 2


## BG 13.21

_puruṣaḥ prakṛti-stho hi bhuṅkte prakṛtijān guṇān | kāraṇaṃ guṇa-saṅgo 'sya sad-asad-yoni-janmasu_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Prakrti (primal nature) is the cause of all action and its instruments — body, organs, and the modifications of pleasure-pain-delusion; purusha (the witnessing self) is only the apparent experiencer of these products. Shankara insists that without the erroneous conjunction (avidya-rupa samyoga) between inert prakrti and the luminous purusha, samsara cannot arise. The root of bondage is thus not action itself but the false identity that makes the jiva (individual soul) believe it is the doer and enjoyer of what prakrti alone produces.


**Words the parser found:**

- **puruṣa** _(seen as puruṣaḥ)_ — _(no MW gloss; not in dictionary)_
- **prakṛti** _(seen as prakṛti)_ — the original producer of (or rather passive power of creating) the material world (consisting of 3…
- **stha** _(seen as sthaḥ)_ — _(no MW gloss; not in dictionary)_
- **hi** _(seen as hi)_ — cl. 5. P. ( Dhātup. xxvii, 11 ) hinoti ( Ved. also hinute , hinvati and hinvati , °te
- **bhuj** _(seen as bhuṅkte)_ — Bujati ( pf. buBoja aor. aBOkzIt fut. Bokzyati and °ktA Gr
- **ja** _(seen as jān)_ — ifc. born or descended from, produced or caused by, born or produced in or at or upon, growing in,…
- **guṇa** _(seen as guṇān)_ — _(no MW gloss; not in dictionary)_
- **kāraṇa** _(seen as kāraṇam)_ — _(no MW gloss; not in dictionary)_
- **saṅga** _(seen as saṅgaḥ)_ — _(no MW gloss; not in dictionary)_
- **idam** _(seen as asya)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **as** _(seen as sat)_ — to be, live, exist, be present
- **asat** _(seen as asat)_ — _(no MW gloss; not in dictionary)_
- **yoni** _(seen as yoni)_ — the womb, uterus, vulva, vagina, female organs of generation, (together with the liNga , a typical…
- **janman** _(seen as janmasu)_ — N. of the 1st lunar mansion, civ


## BG 13.29

_prakṛtyaiva ca karmāṇi kriyamāṇāni sarvaśaḥ | yaḥ paśyati tathātmānam akartāraṃ sa paśyati_


**Śaṅkara/advaita reading (so you know what the verse says):**
> All actions are performed entirely by prakrti (primordial nature); the Self — pure awareness, changeless — does not act. Sankara insists: the ajnani (ignorant one) repeatedly kills his own atman by misidentifying it with the body-mind complex, taking up each new birth as a fresh false self. The one who truly sees the Self as akarta (non-agent), ever-identical across all beings, neither injures the Self by superimposition nor accumulates karma — and thus attains para gati, liberation named moksa.


**Words the parser found:**

- **prakṛti** _(seen as prakṛtyā)_ — the original producer of (or rather passive power of creating) the material world (consisting of 3…
- **eva** _(seen as eva)_ — (√ i , Uṇ. i, 152
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **karman** _(seen as karmāṇi)_ — the object (it stands either in the acc
- **kṛ** _(seen as kriyamāṇāni)_ — cl. 2. P. 2. sg. karzi du. kfTas pl. kfTa
- **sarvaśas** _(seen as sarvaśas)_ — _(no MW gloss; not in dictionary)_
- **yad** _(seen as yaḥ)_ — _(no MW gloss; not in dictionary)_
- **dṛś** _(seen as paśyati)_ — _(no MW gloss; not in dictionary)_
- **tathā** _(seen as tathā)_ — _(no MW gloss; not in dictionary)_
- **ātman** _(seen as ātmānam)_ — the breath
- **akartṛ** _(seen as akartāram)_ — _(no MW gloss; not in dictionary)_
- **tad** _(seen as sa)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…


## BG 14.11

_sarva-dvāreṣu dehe 'smin prakāśa upajāyate | jñānaṃ yadā tadā vidyād vivṛddhaṃ sattvam ity uta_


**Śaṅkara/advaita reading (so you know what the verse says):**
> When the inner faculty (antahkarana) projects its modification through all the gates of perception — the ears and other sense-organs (shrotra-adi), which are the doors of the self's apprehension — that very cognitive luminosity is what is called knowledge (jnana). Recognize this light as the sign (linga) that sattva has risen dominant in the body. The light is not the self; it is the index of sattva's increase, useful as a diagnostic, not as an object of attachment.


**Words the parser found:**

- **sarva** _(seen as sarva)_ — whole, entire, all, every ( m. sg. ‘every one’
- **dvāra** _(seen as dvāreṣu)_ — _(no MW gloss; not in dictionary)_
- **deha** _(seen as dehe)_ — the body, TĀr
- **idam** _(seen as asmin)_ — idam often refers to something immediately following, whereas etad points to what precedes ( SrutvE…
- **prakāśa** _(seen as prakāśaḥ)_ — _(no MW gloss; not in dictionary)_
- **upajan** _(seen as upajāyate)_ — _(no MW gloss; not in dictionary)_
- **jñāna** _(seen as jñānam)_ — the higher knowledge (derived from meditation on the one Universal Spirit), ŚāṅkhŚr. xiii
- **yadā** _(seen as yadā)_ — when, at what time, whenever (generally followed by the correlatives tadA , tatas , tarhi , in Veda…
- **tadā** _(seen as tadā)_ — at that time, then, in that case (often used redundantly, after tatas or purA or before aTa
- **vid** _(seen as vidyāt)_ — vetti ( vidmahe , Br
- **vivṛdh** _(seen as vivṛddham)_ — _(no MW gloss; not in dictionary)_
- **sattva** _(seen as sattvam)_ — being, existence, entity, reality ( ISvara-s ° , ‘the existence of a Supreme Being’), TS. &c. &c
- **iti** _(seen as iti)_ — See √ i above
- **uta** _(seen as uta)_ — or, utrum-an ( kaTam nirRIyate kiM syAn nizkAraRo banDur uta viSvAsa-GAtakaH , how can it be…


## BG 14.12

_lobhaḥ pravṛttir ārambhaḥ karmaṇām aśamaḥ spṛhā | rajasy etāni jāyante vivṛddhe bharatarṣabha_


**Śaṅkara/advaita reading (so you know what the verse says):**
> When rajas (the guna of agitation) intensifies, five signs arise: lobha (greed — coveting another's wealth), pravrtti (general restless activity), arambha (initiating karma-laden projects), asama (absence of quietude — the surge of harsaraga), and sprha (craving for all objects indiscriminately). Sankara reads each term diagnostically: these are linga (marks) that expose which guna dominates, not moral failures in themselves. For the jnana-marga aspirant, recognising these as rajasic signatures is the first move toward niskama-karma and ultimately toward viveka-vairagya that prepares the chitt…


**Words the parser found:**

- **lobha** _(seen as lobhaḥ)_ — _(no MW gloss; not in dictionary)_
- **pravṛtti** _(seen as pravṛttiḥ)_ — the multiplier, W. ( w.r. for pra-kfti ?)
- **ārambha** _(seen as ārambhaḥ)_ — the commencement of the action which awakens an interest in the progress of the principal plot,…
- **karman** _(seen as karmaṇām)_ — the object (it stands either in the acc
- **aśama** _(seen as aśamaḥ)_ — _(no MW gloss; not in dictionary)_
- **spṛhā** _(seen as spṛhā)_ — eager desire, desire, covetousness, envy, longing for, pleasure or delight in ( dat. , gen. loc. ,…
- **rajas** _(seen as rajasi)_ — the second of the three Guṇa s or qualities (the other two being sattva , goodness, and tamas ,…
- **etad** _(seen as etāni)_ — this, this here, here (especially as pointing to what is nearest to the speaker, eza bARaH , this…
- **jan** _(seen as jāyante)_ — to generate, beget, produce, create, cause
- **vivṛdh** _(seen as vivṛddhe)_ — _(no MW gloss; not in dictionary)_
- **bharata** _(seen as bharata)_ — _(no MW gloss; not in dictionary)_
- **ṛṣabha** _(seen as ṛṣabha)_ — _(no MW gloss; not in dictionary)_


## BG 14.20

_guṇān etān atītya trīn dehī deha-samudbhavān | janma-mṛtyu-jarā-duḥkhair vimukto 'mṛtam aśnute_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The embodied one (dehin), by transcending while still living (jivan) these three gunas — sattva, rajas, tamas — which are the seed-causes (bija-bhuta) of bodily birth, becomes liberated even now from birth, death, old age and sorrow. Śaṅkara insists the transcendence is not post-mortem but accomplished through discernment of the Self's non-relation to maya's adjuncts (mायोपाधि). Thus 'amrita' means reaching the state of Brahman (mad-bhavam adhigacchati) — immortality is not gained but recognized as one's own nature.


**Words the parser found:**

- **guṇa** _(seen as guṇān)_ — _(no MW gloss; not in dictionary)_
- **etad** _(seen as etān)_ — this, this here, here (especially as pointing to what is nearest to the speaker, eza bARaH , this…
- **atī** _(seen as atītya)_ — cl. 2. P. aty-eti , -etum , to pass by, elapse, pass over, overflow
- **tri** _(seen as trīn)_ — _(no MW gloss; not in dictionary)_
- **dehin** _(seen as dehī)_ — _(no MW gloss; not in dictionary)_
- **deha** _(seen as deha)_ — the body, TĀr
- **samudbhava** _(seen as samudbhavān)_ — existence, production, origin ( ifc. either ‘arisen or produced from’ or ‘being the source of’)
- **janman** _(seen as janma)_ — N. of the 1st lunar mansion, civ
- **mṛtyu** _(seen as mṛtyu)_ — death, dying
- **jarā** _(seen as jarā)_ — the act of becoming old, old age, i, 140, 8
- **duḥkha** _(seen as duḥkhaiḥ)_ — uneasy, uncomfortable, unpleasant, difficult, R
- **vimuc** _(seen as vimuktaḥ)_ — _(no MW gloss; not in dictionary)_
- **amṛta** _(seen as amṛtam)_ — not dead
- **aś** _(seen as aśnute)_ — _(no MW gloss; not in dictionary)_


## BG 15.2

_adhaś cordhvaṃ prasṛtās tasya śākhā guṇa-pravṛddhā viṣaya-pravālāḥ | adhaś ca mūlāny anusaṃtatāni karmānubandhīni manuṣya-loke_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The branches of this ashvattha (samsara-tree) — the world-appearances — stretch downward through animal births and upward through Brahmaloka, fattened by the three gunas (sattva, rajas, tamas) which are the material cause (upadana-karana) of all embodiment, with sense-objects (vishaya) as their tender shoots. These are not independent realities but superimpositions upon the one Brahman, mistaken for substance just as a shoot is mistaken for the tree itself. Below, in the human world specifically, subsidiary roots proliferate — the volitional impressions (vasana) born of desire and aversion fro…


**Words the parser found:**

- **adhas** _(seen as adhas)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **ūrdhvam** _(seen as ūrdhvam)_ — _(no MW gloss; not in dictionary)_
- **prasṛ** _(seen as prasṛtāḥ)_ — and sarati (sometimes also Ā. °te ), to move forwards, advance (‘for’ or ‘against’ acc. ), proceed…
- **tad** _(seen as tasya)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **śākhā** _(seen as śākhāḥ)_ — _(no MW gloss; not in dictionary)_
- **guṇa** _(seen as guṇa)_ — _(no MW gloss; not in dictionary)_
- **pravṛdh** _(seen as pravṛddhāḥ)_ — _(no MW gloss; not in dictionary)_
- **viṣaya** _(seen as viṣaya)_ — _(no MW gloss; not in dictionary)_
- **pravāla** _(seen as pravālāḥ)_ — a young shoot, sprout, new leaf or branch (to which feet and lips are often compared)
- **mūla** _(seen as mūlāni)_ — ‘firmly fixed’, a root (of any plant or tree
- **anusaṃtan** _(seen as anusaṃtatāni)_ — _(no MW gloss; not in dictionary)_
- **karman** _(seen as karma)_ — the object (it stands either in the acc
- **anubandhin** _(seen as anubandhīni)_ — _(no MW gloss; not in dictionary)_
- **manuṣya** _(seen as manuṣya)_ — _(no MW gloss; not in dictionary)_
- **loka** _(seen as loke)_ — the inhabitants of the world, mankind, folk, people (sometimes opp. to ‘king’)


## BG 15.8

_śarīraṃ yad avāpnoti yac cāpy utkrāmatīśvaraḥ | gṛhītvaitāni saṃyāti vāyur gandhān ivāśayāt_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The jiva (living self), who is the lord (ishvara) of the body-aggregate, carries the mind and the five senses when it departs from one body and enters another — just as wind carries subtle scent-particles from their source. Shankara reads the second half of the verse first by logical necessity: the dragging-away (karshati) precedes the arrival in a new body, so departure is primary, then arrival. The jiva is not truly independent; it moves under the force of karma, dragging these six (mind-as-sixth plus the five senses) not by sovereign choice but as apparent actor within the phenomenal order.


**Words the parser found:**

- **śarīra** _(seen as śarīram)_ — _(no MW gloss; not in dictionary)_
- **yad** _(seen as yat)_ — _(no MW gloss; not in dictionary)_
- **avāp** _(seen as avāpnoti)_ — to reach, attain, obtain, gain, get, Up
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **api** _(seen as api)_ — and, also, moreover, besides, assuredly, surely
- **utkram** _(seen as utkrāmati)_ — P. (and rarely Ā. ) -krAmati , -kramati ( Ved. impf. 3. pl. -akraman , AV. iv, 3, 1 ), -te ( pf. 3.…
- **īśvara** _(seen as īśvaraḥ)_ — _(no MW gloss; not in dictionary)_
- **grah** _(seen as gṛhītvā)_ — to seize, take (by the hand, pARO or kare , exceptionally pARim (double acc. ), i, 125, 1
- **etad** _(seen as etāni)_ — this, this here, here (especially as pointing to what is nearest to the speaker, eza bARaH , this…
- **saṃyā** _(seen as saṃyāti)_ — _(no MW gloss; not in dictionary)_
- **vāyu** _(seen as vāyuḥ)_ — wind, air (as one of the 5 elements
- **gandha** _(seen as gandhān)_ — _(no MW gloss; not in dictionary)_
- **iva** _(seen as iva)_ — _(no MW gloss; not in dictionary)_
- **āśaya** _(seen as āśayāt)_ — _(no MW gloss; not in dictionary)_


## BG 15.12

_yad āditya-gataṃ tejo jagad bhāsayate 'khilam | yac candramasi yac cāgnau tat tejo viddhi māmakam_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The luminosity (tejas) dwelling in the sun that illuminates the entire world, the luminosity in the moon, the luminosity in fire — know all that to be Mine, the light of Visnu. Sankara reads 'tejas' as consciousness-light (caitanya-atmaka jyotis): the same awareness that shines equally through all beings appears more manifestly in the sun and moon only because their sattva-guna is exceedingly pure, just as a face is reflected in a mirror but not in wood — the face itself is unchanged, only the medium differs.


**Words the parser found:**

- **yad** _(seen as yat)_ — _(no MW gloss; not in dictionary)_
- **āditya** _(seen as āditya)_ — N. of a constellation, the seventh lunar mansion
- **gam** _(seen as gatam)_ — : cl. 3. P. jaganti ( Naigh. ii, 14
- **tejas** _(seen as tejaḥ)_ — the sharp edge (of a knife &c.), point or top of a flame or ray, glow, glare, splendour,…
- **jagant** _(seen as jagat)_ — _(no MW gloss; not in dictionary)_
- **bhāsay** _(seen as bhāsayate)_ — _(no MW gloss; not in dictionary)_
- **akhila** _(seen as akhilam)_ — _(no MW gloss; not in dictionary)_
- **candramas** _(seen as candramasi)_ — the moon, deity of the moon (considered as a Dānava , i, 2534
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **agni** _(seen as agnau)_ — fire, sacrificial fire (of three kinds, Gārhapatya , Āhavanīya , and Dakṣiṇa )
- **tad** _(seen as tat)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **vid** _(seen as viddhi)_ — vetti ( vidmahe , Br
- **māmaka** _(seen as māmakam)_ — my, mine


## BG 16.5

_daivī saṃpad vimokṣāya nibandhāyāsurī matā | mā śucaḥ saṃpadaṃ daivīm abhijāto 'si pāṇḍava_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The daivi (divine) sampad (endowment) is for vimoksha (liberation) from samsara-bandhana (the bondage of transmigration); the asuri (demonic) sampad is for nibandha (firm bondage). Shankara notes that on hearing this, Arjuna inwardly deliberated whether he belonged to the demonic or divine endowment — and Krishna reads that inner anxiety. The Lord reassures him: grieve not, for you are born marked for the daivi sampad, your welfare is assured.


**Words the parser found:**

- **daiva** _(seen as daivī)_ — belonging to or coming from the gods, divine, celestial, AV
- **sampad** _(seen as saṃpad)_ — to become thoroughly, Pāṇ. v, 4, 53
- **vimokṣa** _(seen as vimokṣāya)_ — _(no MW gloss; not in dictionary)_
- **nibandha** _(seen as nibandhāya)_ — _(no MW gloss; not in dictionary)_
- **āsura** _(seen as āsurī)_ — _(no MW gloss; not in dictionary)_
- **man** _(seen as matā)_ — manute , manyate ( ep. also °ti
- **mā** _(seen as mā)_ — m. time
- **śuc** _(seen as śucaḥ)_ — _(no MW gloss; not in dictionary)_
- **abhijan** _(seen as abhijātaḥ)_ — to be born for or to, i, 168, 2 , &c
- **as** _(seen as asi)_ — to be, live, exist, be present
- **pāṇḍava** _(seen as pāṇḍava)_ — _(no MW gloss; not in dictionary)_


## BG 16.10

_kāmam āśritya duṣpūraṃ dambha-māna-madānvitāḥ | mohād gṛhītvāsad-grāhān pravartante 'śucivratāḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> The asura-natured person takes refuge in kama (desire) — specifically an insatiable craving that can never be filled — and proceeds through the world armed with dambha (ostentation), mana (arrogance), and mada (intoxication with status). Gripped by moha (delusion, lack of viveka), they embrace asat-graha (false convictions — literally wrong-grasping) as if they were valid. Their vratas (observances) are ashuchi (impure), because without the discrimination that prepares the ground for jnana, even religious practice becomes a vehicle for ego-reinforcement rather than its dissolution.


**Words the parser found:**

- **kāma** _(seen as kāmam)_ — desirous of, desiring, having a desire or intention ( go-k ° , Darma-k °
- **āśri** _(seen as āśritya)_ — _(no MW gloss; not in dictionary)_
- **duṣpūra** _(seen as duṣpūram)_ — _(no MW gloss; not in dictionary)_
- **dambha** _(seen as dambha)_ — _(no MW gloss; not in dictionary)_
- **māna** _(seen as māna)_ — opinion, notion, conception, idea, Tattvas. ( Atma-m ° )
- **mada** _(seen as mada)_ — sexual desire or enjoyment, wantonness, lust, ruttishness, rut ( of an elephant)
- **anvita** _(seen as anvitāḥ)_ — _(no MW gloss; not in dictionary)_
- **moha** _(seen as mohāt)_ — loss of consciousness, bewilderment, perplexity, distraction, infatuation, delusion, error, folly,…
- **grah** _(seen as gṛhītvā)_ — to seize, take (by the hand, pARO or kare , exceptionally pARim (double acc. ), i, 125, 1
- **asat** _(seen as asat)_ — _(no MW gloss; not in dictionary)_
- **grāha** _(seen as grāhān)_ — ifc. seizing, holding, catching, receiving, Yājñ. ii, 51
- **pravṛt** _(seen as pravartante)_ — have anything ( acc. ), : Caus. -vartayati , to cause to turn or roll, set in motion
- **aśuci** _(seen as aśuci)_ — _(no MW gloss; not in dictionary)_
- **vrata** _(seen as vratāḥ)_ — will, command, law, ordinance, rule


## BG 16.17

_ātma-saṃbhāvitāḥ stabdhā dhana-māna-madānvitāḥ | yajante nāma-yajñais te dambhenāvidhi-pūrvakam_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Those who are self-conceited (atma-sambhavita) — esteemed by themselves alone as possessed of all virtues, not by the wise — remain rigid (stabdha), bowing to none. Inflated by wealth and the pride and arrogance that wealth occasions, they perform sacrifices that are sacrifices in name only (nama-yajna), devoid of the prescribed auxiliary rites (vidhi-vihita-anga-itikartavyata) entirely absent. This they do through mere hypocrisy (dambha), bearing religion as a banner — not through faith or genuine renunciation that prepares the mind for knowledge of Brahman.


**Words the parser found:**

- **ātman** _(seen as ātma)_ — the breath
- **sambhāvay** _(seen as saṃbhāvitāḥ)_ — _(no MW gloss; not in dictionary)_
- **stambh** _(seen as stabdhāḥ)_ — cl. 5. 9. P. ( Dhātup. xxxi, 7 ) staBnoti , staBnAti ( Pāṇ. iii, 1, 82 ), or cl. 1. Ā. ( x, 26 )…
- **dhana** _(seen as dhana)_ — _(no MW gloss; not in dictionary)_
- **māna** _(seen as māna)_ — opinion, notion, conception, idea, Tattvas. ( Atma-m ° )
- **mada** _(seen as mada)_ — sexual desire or enjoyment, wantonness, lust, ruttishness, rut ( of an elephant)
- **anvita** _(seen as anvitāḥ)_ — _(no MW gloss; not in dictionary)_
- **yaj** _(seen as yajante)_ — yajati , °te (1. sg. yajase , viii, 25, 1
- **nāman** _(seen as nāma)_ — a characteristic mark or sign, form, nature, kind, manner
- **yajña** _(seen as yajñaiḥ)_ — N. of the reputed author of x, 130 , Anukr
- **tad** _(seen as te)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **dambha** _(seen as dambhena)_ — _(no MW gloss; not in dictionary)_
- **a** _(seen as a)_ — _(no MW gloss; not in dictionary)_
- **vidhi** _(seen as vidhi)_ — _(no MW gloss; not in dictionary)_
- **pūrvaka** _(seen as pūrvakam)_ — _(no MW gloss; not in dictionary)_


## BG 17.5

_aśāstra-vihitaṃ ghoraṃ tapyante ye tapo janāḥ | dambhāhaṃkāra-saṃyuktāḥ kāma-rāga-balānvitāḥ_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Those who perform austerities not sanctioned by scripture (ashaastra-vihita, 'not ordained by the revealed texts') are engaged in what Shankara calls ghora ('fierce, pain-inflicting') tapas — painful to both the self and other beings. Impelled by dambha (ostentation) and ahankara (ego-arrogation), and driven by the force of kama (desire) and raga (attachment), such persons mistake self-mortification for spiritual discipline. In Shankara's reading, this tapas, being untethered from shruti-authority, generates no purification of the antahkarana and thus cannot serve even as the preparatory karma…


**Words the parser found:**

- **a** _(seen as a)_ — _(no MW gloss; not in dictionary)_
- **śāstra** _(seen as śāstra)_ — _(no MW gloss; not in dictionary)_
- **vidhā** _(seen as vihitam)_ — _(no MW gloss; not in dictionary)_
- **ghora** _(seen as ghoram)_ — _(no MW gloss; not in dictionary)_
- **tap** _(seen as tapyante)_ — cl. 4. Ā. °pyate , to rule, Dhātup. xxvi, 50
- **yad** _(seen as ye)_ — _(no MW gloss; not in dictionary)_
- **tapas** _(seen as tapaḥ)_ — N. of a month intervening between winter and spring, VS
- **jana** _(seen as janāḥ)_ — creature, living being, man, person, race ( paYca janAs , ‘the five races’ = p ° kfzwayas , iii  ,…
- **dambha** _(seen as dambha)_ — _(no MW gloss; not in dictionary)_
- **ahaṃkāra** _(seen as ahaṃkāra)_ — the third of the eight producers or sources of creation, viz. the conceit or conception of…
- **saṃyuj** _(seen as saṃyuktāḥ)_ — to have sexual intercourse, PraśnUp
- **kāma** _(seen as kāma)_ — desirous of, desiring, having a desire or intention ( go-k ° , Darma-k °
- **rāga** _(seen as rāga)_ — the act of colouring or dyeing ( mUrDaja-r ° )
- **bala** _(seen as bala)_ — power, strength, might, vigour, force, validity, ( balAt , ‘forcibly, against one's will, without…
- **anvita** _(seen as anvitāḥ)_ — _(no MW gloss; not in dictionary)_


## BG 17.22

_adeśa-kāle yad dānam apātrebhyaś ca dīyate | asatkṛtam avajñātaṃ tat tāmasam udāhṛtam_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Giving that falls into triple defect — wrong place (adesa, an impure or mleccha-contaminated locale), wrong time (akala, a moment carrying no punya-potential, stripped of sankranti or festival mark), and wrong recipient (apatra, the foolish or thieving) — is declared tamasic. Even where place, time, and recipient are adequate, if the gift is given without honor (asat-krtam: no gentle word, no foot-washing, no worship) and with contempt toward the recipient (avajnatam), that too is tamasic. Sankara's point is diagnostic: tamas here is a compound failure of discretion, not merely stinginess, and…


**Words the parser found:**

- **a** _(seen as a)_ — _(no MW gloss; not in dictionary)_
- **deśa** _(seen as deśa)_ — _(no MW gloss; not in dictionary)_
- **kāla** _(seen as kāle)_ — Ipomoea atropurpurea , Suśr
- **yad** _(seen as yat)_ — _(no MW gloss; not in dictionary)_
- **dāna** _(seen as dānam)_ — distribution of food or of a sacrificial meal
- **apātra** _(seen as apātrebhyaḥ)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **dā** _(seen as dīyate)_ — ifc. ( Pāṇ. iii, 2, 3 ) giving, granting, offering, effecting, producing ( aBI zwa- , ‘giving any…
- **asatkṛ** _(seen as asatkṛtam)_ — _(no MW gloss; not in dictionary)_
- **avajñā** _(seen as avajñātam)_ — to disesteem, have a low opinion of, despise, treat with contempt
- **tad** _(seen as tat)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **tāmasa** _(seen as tāmasam)_ — dark
- **udāhṛ** _(seen as udāhṛtam)_ — _(no MW gloss; not in dictionary)_


## BG 18.23

_niyataṃ saṅgarahitamarāgadveṣataḥ kṛtam | aphalaprepsunā karma yattatsāttvikamucyate_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Action is sattvic when it is niyata (prescribed duty), sanga-rahita (stripped of attachment to doing), and performed without the impulsion of raga (attraction) or dvesha (aversion). Shankara isolates the term aphala-prepsuna precisely: fala-prepsu is one gripped by thirst for results; the sattvic agent is the exact inversion of that thirst. Such karma purifies the inner organ and qualifies the agent for jnana — it is not liberating in itself but clears the field.


**Words the parser found:**

- **niyam** _(seen as niyatam)_ — to stop ( intrans. ), stay, remain
- **saṅga** _(seen as saṅga)_ — _(no MW gloss; not in dictionary)_
- **rahita** _(seen as rahitam)_ — wanting, absent ( below)
- **a** _(seen as a)_ — _(no MW gloss; not in dictionary)_
- **rāga** _(seen as rāga)_ — the act of colouring or dyeing ( mUrDaja-r ° )
- **dveṣa** _(seen as dveṣataḥ)_ — _(no MW gloss; not in dictionary)_
- **kṛ** _(seen as kṛtam)_ — cl. 2. P. 2. sg. karzi du. kfTas pl. kfTa
- **phala** _(seen as phala)_ — fruit ( of trees)
- **prepsu** _(seen as prepsunā)_ — _(no MW gloss; not in dictionary)_
- **karman** _(seen as karma)_ — the object (it stands either in the acc
- **yad** _(seen as yat)_ — _(no MW gloss; not in dictionary)_
- **tad** _(seen as tat)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **sāttvika** _(seen as sāttvikam)_ — spirited, vigorous, energetic
- **vac** _(seen as ucyate)_ — vakti (occurs only in sg. vacmi , vakzi , vakti , and Impv. vaktu


## BG 18.71

_śraddhāvānanasūyaśca śṛṇuyādapi yo naraḥ | so'pi muktaḥ śubhā~llokānprāpnuyātpuṇyakarmaṇām_


**Śaṅkara/advaita reading (so you know what the verse says):**
> Even the person who merely hears this teaching with faith (shraddha) and without envy (asuya) — let alone one who grasps its meaning — is freed from sin and attains the auspicious worlds of those who perform meritorious acts such as the agnihotra. Shankara notes the 'api' (even) marks ascending force: mere hearing surpasses elaborate ritual, how much more so genuine understanding. The teacher's duty is to keep finding new means until the student is established in the truth.


**Words the parser found:**

- **śraddhāvat** _(seen as śraddhāvān)_ — _(no MW gloss; not in dictionary)_
- **anasūya** _(seen as anasūyaḥ)_ — _(no MW gloss; not in dictionary)_
- **ca** _(seen as ca)_ — class of consonants, having the sound of ch in church
- **śru** _(seen as śṛṇuyāt)_ — _(no MW gloss; not in dictionary)_
- **api** _(seen as api)_ — and, also, moreover, besides, assuredly, surely
- **yad** _(seen as yaḥ)_ — _(no MW gloss; not in dictionary)_
- **nara** _(seen as naraḥ)_ — a man, a male, a person ( pl. men, people), TS. &c. &c
- **tad** _(seen as saḥ)_ — m. he f. she n. it, that, this (often correlative of ya generally standing in the preceding clause,…
- **muc** _(seen as muktaḥ)_ — muYcati , °te ( also, mucanti , mucasva
- **śubha** _(seen as śubhān)_ — _(no MW gloss; not in dictionary)_
- **loka** _(seen as lokān)_ — the inhabitants of the world, mankind, folk, people (sometimes opp. to ‘king’)
- **prāp** _(seen as prāpnuyāt)_ — P. Ā. prA pnoti ( irreg. Pot. prA peyam ), to attain to
- **puṇya** _(seen as puṇya)_ — _(no MW gloss; not in dictionary)_
- **karman** _(seen as karmaṇām)_ — the object (it stands either in the acc


---
## Scoring

When done, count: how many lemmas you marked `✗` out of the total. Anything below ~5% means the substrate is publishable. Anything between 5–15% means we tune the rule layer. Above 15% means we need to revisit the parser or its inputs.
