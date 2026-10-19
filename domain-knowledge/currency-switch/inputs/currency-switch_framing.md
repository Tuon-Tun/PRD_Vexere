# Product Framing Pack - Currency Switch

## 1. Framing Summary

| Field | Detail |
|-------|--------|
| Delivery Mode | IDE_FULL_PIPELINE |
| Output Artifacts | Markdown File, DOCX File |
| Domain | currency-switch |
| Feature | Currency Switch |
| Core Objective | Cho khách quốc tế xem giá tham khảo bằng tiền tệ của mình bên cạnh VND trên UI ngoại ngữ, trong khi luôn thanh toán bằng VND, để tăng tỷ lệ hoàn thành đơn mà không tạo rủi ro pháp lý, tài chính hay khiếu nại mới. |
| Research Status | hypothesized, needs validation |

## 2. Jobs To Be Done

### JTBD-01 - Khách inbound xem giá

**Status:** hypothesized, needs validation

Khi xem giá chuyến xe tại Việt Nam trên trang ngoại ngữ, tôi muốn thấy giá bằng tiền tệ của mình bên cạnh VND, để tôi có thể ước lượng chi phí mà không phải tự quy đổi.

### JTBD-02 - Khách inbound sắp thanh toán

**Status:** hypothesized, needs validation

Khi sắp thanh toán, tôi muốn biết chính xác số VND sẽ bị trừ và việc ngân hàng có thể áp tỷ giá, phí riêng, để tôi có thể không bất ngờ khi xem sao kê.

### JTBD-03 - Khách inbound không đọc được tiếng Việt

**Status:** hypothesized, needs validation

Khi tìm và đặt vé mà không đọc được tiếng Việt, tôi muốn đọc toàn bộ trang và địa danh bằng ngôn ngữ của mình hoặc chữ Latin không dấu, để tôi có thể tự tìm chuyến và đặt vé mà không cần hỏi ai.

### JTBD-04 - Khách quay lại hoặc khách mở link chia sẻ

**Status:** hypothesized, needs validation

Khi quay lại Vexere hoặc mở một link được chia sẻ, tôi muốn thấy ngay ngôn ngữ và tiền tệ phù hợp mà không phải chọn lại, để tôi có thể xem giá ngay.

### JTBD-05 - Người chia sẻ link Vexere (marketing, affiliate)

**Status:** hypothesized, needs validation

Khi chia sẻ link Vexere cho khách của một thị trường, tôi muốn link mở trang bằng ngôn ngữ và tiền tệ tôi chỉ định, để tôi có thể cho người nhận thấy đúng thông tin tôi muốn.

### JTBD-06 - Nhân viên CSKH

**Status:** hypothesized, needs validation

Khi khách khiếu nại "giá khác số bị trừ", tôi muốn xem đúng những gì khách đã thấy trên đơn, để tôi có thể xử lý khiếu nại bằng bằng chứng.

### JTBD-07 - Kế toán và Finance analyst

**Status:** hypothesized, needs validation

Khi xuất hoá đơn và lập báo cáo doanh thu, tôi muốn mọi số liệu được ghi nhận bằng VND, để tôi có thể báo cáo mà không bị lẫn số tham khảo.

### JTBD-08 - PO

**Status:** hypothesized, needs validation

Khi mở thêm thị trường hoặc khi có sự cố, tôi muốn bật ngôn ngữ, tiền tệ và tắt tính năng mà không cần phát hành bản mới, để tôi có thể mở rộng an toàn và dừng ngay khi có rủi ro.

### JTBD-09 - Nhân viên vận hành tỷ giá

**Status:** hypothesized, needs validation

Khi thêm cặp tiền hoặc khi có sự cố về tỷ giá, tôi muốn quản lý quy tắc tỷ giá và nguồn tỷ giá mà không cần Dev, để tôi có thể giữ số tham khảo dựa trên tỷ giá đúng và ổn định.

## 3. Business Rules

Quy ước cho cột Example: số viết như trên UI EN (dấu phẩy ngăn nghìn, dấu chấm thập phân); tỷ giá là số VND cho 1 đơn vị ngoại tệ (A-03). Ngôn ngữ, tiền tệ trong ví dụ là giá trị mẫu; danh sách thực tế theo cấu hình của BU (BR-22, A-08). Lúc ra mắt VND là số chính trên mọi bề mặt (BR-06), nên ví dụ hiển thị viết dạng "467,000 VND : ~USD 17.92".

**Formulas, Policies & Limits**

*Thanh toán và doanh thu*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-01 | Tiền thanh toán (settlement) luôn là VND cho mọi khách, trên mọi ngôn ngữ và mọi platform. Tiền tệ tham khảo chỉ để hiển thị, không dùng trong giao dịch, hoá đơn, đối soát hay báo cáo doanh thu. | Khách dùng UI KO, chọn KRW: thấy 470,300 VND : ~KRW 24,818 và bị trừ đúng 470,300 VND. | — | Gốc: BR-S01 |
| BR-02 | Vexere không thu phí quy đổi ngoại tệ. | Đơn 470,300 VND, tiền tệ tham khảo USD: khách trả 470,300 VND, không có dòng phí quy đổi. | BR-01 | Gốc: BR-S02 |
| BR-03 | Hoá đơn VAT luôn bằng VND; số ngoại tệ không xuất hiện trong chỉ tiêu tính thuế. | Đơn 470,300 VND, tiền tệ tham khảo USD: hoá đơn VAT chỉ ghi 470,300 VND. | BR-01 | Gốc: BR-S03 |
| BR-04 | Mọi số liệu doanh thu được ghi nhận bằng số tiền VND; số tham khảo chỉ là thông tin phụ đi kèm. | Đơn 470,300 VND : ~USD 18.05: doanh thu ghi 470,300 VND; USD 18.05 chỉ là thông tin phụ. | BR-01 | Gốc: US-18 |

*Hiển thị số tiền*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-05 | Hiển thị kép một dòng: mọi bề mặt có giá trong phạm vi đợt này (SCR-01 đến SCR-05, SCR-07 đến SCR-11, SCR-15) hiển thị số tham khảo và số VND trên cùng một dòng, dạng "số chính : số phụ". Ngoại tệ khi ở vị trí số phụ có tiền tố "~". Số nào là số chính theo BR-06. | 467,000 VND : ~USD 17.92 | BR-06, BR-07, BR-11, BR-12 | Gốc: BR-D01; 14 điểm hiển thị giá của UI_UX_Requirements |
| BR-06 | Chế độ thứ bậc hiển thị: một cài đặt có 2 chế độ, đổi được mà không cần phát hành bản mới, theo phân quyền BR-79. (1) VND là số chính trên mọi bề mặt. (2) Theo nhóm: nhóm Browse (kết quả tìm kiếm, tìm nhà xe, chi tiết chuyến, chọn ghế, lịch giá, bộ lọc và thanh trượt giá, nhãn giảm giá, trang SEO landing) lấy ngoại tệ làm số chính; nhóm Pay (checkout, thanh toán, email xác nhận, My bookings, hoàn tiền, back office) lấy VND làm số chính. Chế độ lúc ra mắt: (1) VND là số chính trên mọi bề mặt (assumed, A-10). | Chế độ (1): kết quả tìm kiếm 467,000 VND : ~USD 17.92; checkout 470,300 VND : ~USD 18.05. Chế độ (2): kết quả tìm kiếm USD 17.92 : 467,000 VND; checkout 470,300 VND : ~USD 18.05. | BR-05, BR-79 | Gốc: BR-D01, CR-04; quyết định 5 |
| BR-07 | Không bề mặt nào hiện ngoại tệ mà thiếu số VND. | Ô giá không bao giờ chỉ có "~USD 17.92"; luôn kèm 467,000 VND. | BR-05 | Gốc: US-10 |
| BR-08 | Khi tiền tệ hiện hành là VND (UI VI, hoặc khách chọn VND), chỉ hiển thị VND, không có số quy đổi. | UI EN, khách chọn VND: 467,000 VND, không có ~USD. | BR-23 | Gốc: BR-D02 |
| BR-09 | Số lẻ của mỗi tiền tệ theo bảng cố định của Vexere, không theo mặc định của chuẩn định dạng quốc tế (vốn cho IDR, TWD 2 số lẻ). 0 số lẻ: VND, JPY, KRW, IDR, TWD. 2 số lẻ: USD, EUR, SGD, THB, CNY. 3 số lẻ: BHD, KWD, OMR. Tiền tệ không có trong bảng dùng số lẻ chuẩn ISO 4217 của tiền tệ đó. | Giá trị mẫu: 467,000 VND với 1 TWD = 820 VND → 569.51 → TWD 570; với 1 KWD = 85,000 VND → 5.4941 → KWD 5.494; AUD không có trong bảng → 2 số lẻ theo ISO 4217. | BR-10 | Gốc: BR-D03; quyết định 12 |
| BR-10 | Làm tròn half-up (nửa lên, xa số 0) tới số lẻ của tiền tệ (BR-09). Mọi nơi hiển thị dùng cùng một quy tắc làm tròn. | 17.925 → 17.93; 17.924 → 17.92; −2,464.5 → −2,465. | BR-09 | Gốc: CR-03 |
| BR-11 | Mọi số tiền luôn kèm mã ISO 4217 3 chữ cái, không dùng ký hiệu tiền tệ, trên mọi ngôn ngữ, để tránh nhầm ¥ giữa JPY và CNY. | USD 19.96, CNY 127.95; không viết $19.96 hay ¥127.95. | — | Gốc: BR-D04, US-01 |
| BR-12 | Số VND định dạng theo ngôn ngữ UI, mã VND đứng sau số. Mã ngoại tệ đứng trước số. Mỗi ngôn ngữ chỉ có một cách viết số VND trên toàn UI, mọi platform. | EN và VI: 520,000 VND. Ngoại tệ: USD 17.92. Không viết "VND 520,000". | BR-09, BR-11 | Gốc: BR-D05, US-01; quyết định 5 |

*Quy đổi và breakdown*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-13 | Tỷ giá dùng để quy đổi là tỷ giá của cặp tiền XXX/VND trong bảng tỷ giá đang dùng: bảng tỷ giá hiện hành (BR-48), bảng tỷ giá của báo giá trong checkout (BR-66), hoặc bảng tỷ giá lưu trên đơn sau khi đặt (BR-44). Tỷ giá là số VND cho 1 đơn vị ngoại tệ, lấy theo quy tắc tỷ giá của cặp đó (BR-52) và cài đặt buffer BR-14. | Giá trị mẫu: 1 USD = 26,054 VND; 1 KRW = 18.95 VND. | BR-14, BR-44, BR-48, BR-52, BR-66 | Gốc: BR-S02, CR-06 |
| BR-14 | Buffer của quy tắc tỷ giá có áp vào số tham khảo hay không: cài đặt Có/Không cho từng cặp tiền, do nhân viên vận hành tỷ giá chọn trên công cụ cấu hình tỷ giá (BR-78). Mặc định: brief không nêu. Có: quy đổi bằng tỷ giá theo quy tắc, sau buffer (BR-52). Không: quy đổi bằng tỷ giá gốc. | Giá trị mẫu, USD gốc 25,899, buffer 2%: Có → 470,300 / 26,417 = 17.803 → ~USD 17.80. Không → 470,300 / 25,899 = 18.159 → ~USD 18.16. | BR-10, BR-52, BR-78 | Gốc: BR-S02, CR-34; quyết định 6 |
| BR-15 | Công thức quy đổi. Tổng tham khảo = làm tròn(tổng VND sau giảm giá / tỷ giá). Mỗi dòng dương của breakdown (vé, phí, bảo hiểm, dịch vụ thêm) quy đổi và làm tròn độc lập: dòng tham khảo = làm tròn(VND của dòng / tỷ giá). Làm tròn theo BR-09 và BR-10. | 1 USD = 26,054 VND: total 470,300 VND → 18.051 → ~USD 18.05; dòng vé 467,000 VND → 17.924 → ~USD 17.92. | BR-09, BR-10, BR-13, BR-16 | Gốc: CR-06, CR-07 |
| BR-16 | Mọi tính toán nghiệp vụ (voucher %, mức trần, phí) tính bằng VND trước, rồi mới quy đổi kết quả sang tiền tệ tham khảo. | Voucher 10% trên vé 467,000 VND = −46,700 VND, rồi mới quy đổi; không tính 10% trên số USD. | — | Gốc: BR-D06, CR-09 |
| BR-17 | Breakdown luôn cộng khớp total. Đơn có dòng giảm giá: dòng giảm giá gánh phần chênh do làm tròn; giảm giá tham khảo = tổng tham khảo − tổng các dòng dương − tổng các dòng giảm giá khác. Có nhiều dòng giảm giá thì dòng có giá trị tuyệt đối lớn nhất gánh chênh, các dòng giảm giá khác quy đổi độc lập theo BR-15. | 1 KRW = 18.95 VND: vé 467,000 VND → 24,643.80 → 24,644; phí dịch vụ 50,000 VND → 2,638.52 → 2,639; total 470,300 VND → 24,817.94 → 24,818; voucher 10% −46,700 VND → 24,818 − 24,644 − 2,639 = −2,465 (quy đổi độc lập sẽ là −2,464). Kiểm tra: 24,644 + 2,639 − 2,465 = 24,818. | BR-15, BR-16 | Gốc: BR-D06, CR-08 |
| BR-18 | Đơn không có dòng giảm giá: phần chênh do làm tròn (tổng tham khảo − tổng các dòng dương) cộng vào dòng có giá trị VND lớn nhất. | 1 USD = 26,054 VND: vé chặng 1 467,000 VND → 17.92; phí dịch vụ 50,000 VND → 1.92; vé chặng 2 517,000 VND → 19.84; total 1,034,000 VND → 39.687 → 39.69. Chênh 39.69 − (17.92 + 1.92 + 19.84) = +0.01 cộng vào vé chặng 2 → 19.85. Kiểm tra: 17.92 + 1.92 + 19.85 = 39.69. | BR-15 | Gốc: CR-10 |
| BR-19 | Đơn nhiều vé: mỗi dòng breakdown là thành tiền của dòng (đơn giá × số lượng) rồi mới quy đổi. Sơ đồ ghế và chi tiết chuyến quy đổi theo đơn giá. | 1 USD = 26,054 VND: breakdown 2 vé × 467,000 VND = 934,000 VND → 35.849 → ~USD 35.85; sơ đồ ghế hiện ~USD 17.92 mỗi ghế (2 × 17.92 = 35.84 khác 35.85 là đúng quy tắc). | BR-15 | Gốc: CR-11, CR-12 |
| BR-20 | Voucher và khuyến mãi luôn lấy VND làm số chính, ở cả hai chế độ của BR-06. | Chế độ (2): dòng voucher có số chính là −46,700 VND, số phụ là số USD quy đổi. | BR-06 | Gốc: BR-D07 |
| BR-21 | Lọc giá theo tiền tham khảo: giá trị biên khách chọn bằng tiền tệ tham khảo được quy ngược về VND và so sánh bằng VND, nới thêm nửa đơn vị nhỏ nhất của tiền tệ tham khảo (theo số lẻ BR-09, ví dụ USD 0.01, KRW 1) ở hai đầu, để chuyến hiển thị đúng bằng giá trị biên vẫn được giữ. Biên trên VND = (biên trên + 0.5 × đơn vị) × tỷ giá. Biên dưới VND = (biên dưới − 0.5 × đơn vị) × tỷ giá. Chuyến được giữ khi biên dưới VND ≤ giá VND ≤ biên trên VND. | 1 USD = 26,054 VND. Lọc ≤ USD 20: biên trên = 20.005 × 26,054 = 521,210.27 VND → giữ chuyến 521,100 VND (~USD 20.00), loại chuyến 521,250 VND (~USD 20.01). Lọc ≥ USD 15: biên dưới = 14.995 × 26,054 = 390,679.73 VND → giữ chuyến 390,700 VND (~USD 15.00). | BR-09, BR-10, BR-13 | Gốc: BR-D08, CR-32 |

*Ngôn ngữ và tiền tệ*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-22 | Ngôn ngữ và tiền tệ là hai danh sách riêng, kèm bảng quốc gia → tiền tệ. Ngôn ngữ, tiền tệ nào được bật và bảng quốc gia → tiền tệ do BU cấu hình (DEP-14), theo phân quyền BR-76, không cần phát hành bản mới. Ngôn ngữ không có trong danh sách đang bật thì dùng EN. Lúc ra mắt áp dụng cho vertical Bus. | Giá trị mẫu (cấu hình ví dụ của PRD gốc): ngôn ngữ VI, EN, ZH, KO, TH; bảng quốc gia → tiền tệ có VN → VND, US → USD, KR → KRW, TW → TWD. Trình duyệt ưu tiên ja, JA chưa bật → EN. | BR-76 | Gốc: BR-N01; quyết định 2; A-08 |
| BR-23 | Phạm vi tiền tệ của ngôn ngữ: mỗi ngôn ngữ khai báo danh sách tiền tệ được dùng và một tiền tệ chính (BU cấu hình, BR-22). Danh sách thực tế khách chọn được = tiền tệ của ngôn ngữ ∩ tiền tệ đang bật ∩ tiền tệ có trong bảng tỷ giá hiện hành, luôn có VND. Picker tiền tệ chỉ cho chọn trong danh sách thực tế. Mỗi tiền tệ trong danh sách cần một quy tắc tỷ giá đang bật (BR-52). Ngôn ngữ VI chỉ có VND. Muốn xem tiền tệ ngoài phạm vi, khách chuyển sang ngôn ngữ tương ứng hoặc EN. | Giá trị mẫu: ZH: CNY, TWD (chính CNY); KO: KRW, USD (chính KRW); TH: THB, USD (chính THB); VI: VND. Danh sách thực tế của KO: KRW, USD, VND; quy tắc KRW/VND bị tắt (BR-53) → USD, VND. | BR-22, BR-48, BR-52, BR-53 | Gốc: BR-N02, US-06; A-08 |
| BR-24 | Đổi ngôn ngữ thì tiền tệ được xác định lại trong phạm vi tiền tệ của ngôn ngữ mới, theo thứ tự ưu tiên BR-26. | Khách ở Hàn Quốc đang EN + EUR, đổi sang KO → EUR ngoài phạm vi KO → KRW. | BR-23, BR-26 | Gốc: US-05 |
| BR-25 | Tiền tệ mặc định, xét theo thứ tự, chỉ nhận ứng viên thuộc phạm vi tiền tệ của ngôn ngữ (BR-23): (1) tiền tệ của quốc gia nơi khách truy cập theo bảng quốc gia → tiền tệ (web: theo vị trí truy cập; app: theo vùng của thiết bị); (2) tiền tệ chính của ngôn ngữ; (3) với EN: USD. Không ứng viên nào hợp lệ thì chỉ hiển thị VND (CB-02). | EN ở Mỹ → USD; EN ở Việt Nam → VND (đổi được trên picker); EN ở Pháp → EUR nếu đang bật, không thì USD; ZH ở Đài Loan → TWD; ZH ở Việt Nam → CNY; KO ở Mỹ → USD; KO ở Hàn Quốc hoặc Việt Nam → KRW. | BR-22, BR-23 | Gốc: BR-N03 |
| BR-26 | Thứ tự ưu tiên xác định ngôn ngữ và tiền tệ (xác định riêng từng giá trị, cùng một thứ tự): (1) thao tác của khách trong phiên; (2) tham số trên link, chỉ cho phiên đó, không lưu (BR-31); (3) lựa chọn chủ động gần nhất giữa hồ sơ và thiết bị (BR-32); (4) giá trị tự nhận diện lần đầu (BR-29); (5) mặc định: EN cho ngôn ngữ, BR-25 cho tiền tệ. Ngôn ngữ được xác định trước; tiền tệ phải thuộc phạm vi của ngôn ngữ hiện hành (BR-23), không thì xét ứng viên kế tiếp (BR-33, BR-34). Ngôn ngữ VI luôn dùng VND. Giá trị tự nhận diện không phải lựa chọn chủ động. | Khách đã lưu chủ động EN + USD, mở link chỉ định KO + KRW → phiên đó là KO + KRW; phiên sau quay lại EN + USD. | BR-23, BR-25, BR-29, BR-31, BR-32, BR-33, BR-34 | Gốc: BR-N04, CR-13 |
| BR-27 | Picker tiền tệ của EN có nhóm Gợi ý gồm, theo thứ tự: tiền tệ của quốc gia, tiền tệ khách đã chọn trước đây, tiền tệ của các đơn đã thanh toán, USD; tối đa 4, không trùng. Sau đó là nhóm Tất cả, xếp A–Z theo mã ISO. Cả hai nhóm chỉ gồm tiền tệ thuộc danh sách thực tế (BR-23). | Giá trị mẫu: khách EN ở Hàn Quốc, trước đây chọn EUR, có đơn đã thanh toán với tiền tệ tham khảo USD → Gợi ý: KRW, EUR, USD (USD không lặp). Tất cả: AUD, CNY, EUR, JPY, KRW, ... | BR-23 | Gốc: BR-N05, US-06 |
| BR-28 | Trên web, ngôn ngữ của trang theo ngôn ngữ trong đường dẫn (ví dụ /en-US/). Đường dẫn không có ngôn ngữ thì tự nhận diện (BR-29) và dẫn tới đường dẫn có ngôn ngữ tương ứng. Bot của công cụ tìm kiếm không bị tự nhận diện và luôn nhận giá VND. | Mở /en-US/ → EN. Khách mới ở Hàn Quốc mở đường dẫn không có ngôn ngữ, trình duyệt ưu tiên ko → dẫn tới /ko-KR/. Bot tìm kiếm mở /en-US/ → trang EN, giá chỉ VND. | BR-29 | Gốc: BR-N06 |
| BR-29 | Tự nhận diện cho khách mới: chỉ chạy khi khách chưa có ngôn ngữ, tiền tệ đã lưu và chưa có hồ sơ; không chạy với bot công cụ tìm kiếm; trên app chạy ở lần mở đầu tiên. Ngôn ngữ: web theo tham số ngôn ngữ trên link > ngôn ngữ trong đường dẫn > ngôn ngữ ưu tiên đầu tiên của trình duyệt; app theo ngôn ngữ thiết bị; không khớp ngôn ngữ nào đang bật → EN. Tiền tệ: theo BR-25; không xác định được quốc gia thì bỏ qua bước (1) của BR-25. Không xác định được tín hiệu nào (VPN, thiếu thông tin) → EN + USD. Kết quả được lưu là giá trị không chủ động (BR-31). | Web, trình duyệt ưu tiên th, truy cập từ Thái Lan → TH + THB. App, thiết bị dùng ja (JA chưa bật), ở Úc → EN + AUD nếu đang bật, không thì USD. VPN, không xác định → EN + USD. | BR-22, BR-25, BR-30, BR-31 | Gốc: BR-N09, CR-17 đến CR-21 |
| BR-30 | Bảng quyết định cho khách mới (quốc gia / ngôn ngữ trình duyệt hoặc thiết bị → ngôn ngữ, tiền tệ), theo BR-29 và BR-25: VN / vi → VI, VND (không có picker tiền tệ); VN / en → EN, VND (expat, khách quốc tế tại VN; đổi được sang tiền tệ khác); VN / zh, ko, th → ZH, KO, TH với CNY, KRW, THB; US / en → EN, USD; CN / zh-CN → ZH, CNY; TW / zh-TW → ZH (giản thể), TWD nếu đang bật, không thì CNY; KR / ko → KO, KRW; TH / th → TH, THB; KR / en → EN, KRW (EN lấy tiền tệ theo quốc gia); JP / ja (chưa có trong cấu hình) → EN, JPY nếu đang bật, không thì USD; AU / en → EN, AUD nếu đang bật, không thì USD; FR, DE / fr, de → EN, EUR nếu đang bật, không thì USD; ngoài VN / vi → VI, VND (Việt kiều); không xác định hoặc VPN → EN, USD; US / ko → KO, USD (USD thuộc phạm vi KO). | Mọi dòng là giá trị mẫu theo cấu hình ví dụ của PRD gốc; ngôn ngữ, tiền tệ thực tế theo cấu hình của BU (A-08). | BR-25, BR-29 | Gốc: BR-N10; A-08 |
| BR-31 | Lưu lựa chọn: ngôn ngữ và tiền tệ lưu riêng; mỗi giá trị kèm đánh dấu là lựa chọn chủ động hay tự nhận diện và thời điểm chọn. Sau tự nhận diện, cả hai được lưu là không chủ động; phiên sau dùng lại, không tự nhận diện lại. Khách đổi trên picker → lưu là lựa chọn chủ động kèm thời điểm, đồng bộ lên hồ sơ nếu đã đăng nhập. Guest lưu trên thiết bị; khách đã đăng nhập lưu cả trên hồ sơ để giữ qua các thiết bị. Tham số trên link không được lưu vào thiết bị hay hồ sơ. | Guest lần đầu được tự nhận diện EN + USD (không chủ động); đổi sang EUR lúc 10:00 → EUR chủ động, 10:00; hôm sau mở lại → EN + EUR, không tự nhận diện lại. | BR-26, BR-29 | Gốc: BR-N11, CR-21, US-07, US-09 |
| BR-32 | Khi giá trị trên thiết bị và trên hồ sơ khác nhau (xét riêng ngôn ngữ và tiền tệ): lựa chọn chủ động thắng giá trị tự nhận diện; hai lựa chọn chủ động thì cái mới hơn thắng và được đồng bộ lên hồ sơ khi đăng nhập; hai giá trị không chủ động thì hồ sơ thắng. | Thiết bị USD chủ động lúc 10:00 hôm nay, hồ sơ EUR chủ động hôm qua → đăng nhập → USD, hồ sơ cập nhật USD. Thiết bị KRW tự nhận diện, hồ sơ USD chủ động → USD. Thiết bị VND tự nhận diện, hồ sơ KRW tự nhận diện → KRW. | BR-31 | Gốc: CR-14 |
| BR-33 | Tiền tệ đã lưu nằm ngoài phạm vi tiền tệ của ngôn ngữ hiện hành không bị xoá, chỉ bị bỏ qua cho tới khi khách quay về ngôn ngữ có phạm vi chứa nó. | EN + RUB → chuyển KO → KRW (RUB ngoài phạm vi KO) → quay lại EN → RUB. | BR-23, BR-26 | Gốc: CR-15, US-07 |
| BR-34 | Tham số tiền tệ trên link nằm ngoài phạm vi tiền tệ của ngôn ngữ hiện hành thì bị bỏ qua; tiền tệ được xác định theo ứng viên kế tiếp của BR-26. | Link chỉ định KO + JPY → JPY bị bỏ qua → KO + tiền tệ theo ứng viên kế tiếp, ví dụ KRW. | BR-23, BR-26 | Gốc: US-09 |
| BR-35 | Một ngôn ngữ chỉ được bật khi bản dịch của ngôn ngữ đó đã được đưa lên hệ thống. | Bản dịch JA chưa được đưa lên → không bật được JA. | BR-22, BR-76 | Gốc: BR-N12 |
| BR-36 | Mọi thay đổi cấu hình ngôn ngữ, tiền tệ và bảng quốc gia → tiền tệ được ghi lịch sử: người thực hiện, thời điểm, giá trị cũ, giá trị mới. | Giá trị mẫu: đổi tiền tệ chính của ZH từ CNY sang TWD → lịch sử ghi người đổi, thời điểm, CNY, TWD. | BR-22 | Gốc: BR-N12, US-20 |

*Địa danh*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-37 | Địa danh trên UI ngoại ngữ (Phase 1): mọi địa danh Bus (bến xe, trạm dừng, điểm đón trả) được chuẩn hoá thành không dấu theo BR-38, dùng chung cho mọi ngôn ngữ ngoại ngữ, kể cả ngôn ngữ thêm sau. Tên bản địa theo từng ngôn ngữ cho Top 50 điểm đến nằm ngoài phạm vi đợt này. | UI EN, KO, TH đều hiện "Ben xe Mien Dong". | BR-38 | Gốc: BR-N07, US-02; quyết định 3 |
| BR-38 | Cách chuẩn hoá không dấu: bỏ dấu tiếng Việt và chuyển "đ/Đ" thành "d/D". | "Đà Lạt" → "Da Lat"; "Bến xe Miền Đông" → "Ben xe Mien Dong". | — | Gốc: BR-N08 |

*Checkout*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-39 | Số VND giữ cố định trong một báo giá: trước màn thanh toán, đổi ngôn ngữ hoặc tiền tệ chỉ đổi tiền tệ tham khảo; tỷ giá vẫn lấy từ bảng tỷ giá của báo giá; số VND và thời điểm hết giữ chỗ không đổi. | Báo giá 470,300 VND, bảng tỷ giá có 1 USD = 26,054 VND và 1 KRW = 18.95 VND. Đổi USD → KRW: 470,300 VND : ~USD 18.05 thành 470,300 VND : ~KRW 24,818; số VND vẫn 470,300. | BR-13, BR-15, BR-66 | Gốc: BR-C01, CR-23 |
| BR-40 | Ngôn ngữ và tiền tệ đổi được từ trang kết quả tìm kiếm tới bước nhập thông tin hành khách; ở màn thanh toán thì không đổi được. | Ở bước nhập thông tin: đổi USD → KRW được. Ở màn thanh toán: không đổi được. | BR-39 | Gốc: BR-C07 |
| BR-41 | Bản dịch Payment Notice (MSG-08, MSG-09) của một ngôn ngữ chưa được duyệt thì hiển thị bản EN. | Bản dịch TH của Payment Notice chưa được duyệt → khách dùng UI TH thấy Payment Notice bản EN. | — | Gốc: US-13 |
| BR-42 | Khi lưu đơn, số tham khảo trên đơn luôn được Vexere tính lại từ bảng tỷ giá của báo giá theo BR-15 đến BR-19, không lấy số hiển thị trên thiết bị của khách; 100% đơn có số tham khảo được tính lại. | Thiết bị của khách hiển thị ~USD 18.06 (sai lệch); đơn vẫn lưu 470,300 / 26,054 = 18.051 → ~USD 18.05. | BR-13, BR-15, BR-17, BR-18, BR-19, BR-66 | Gốc: CR-25, NFR-04 |
| BR-43 | Đơn chỉ lưu số tham khảo khi màn thanh toán đã hiển thị số tham khảo cho khách; nếu không, đơn không có số tham khảo (CB-05) (assumed, A-12). | Màn thanh toán chỉ hiển thị VND vì bảng tỷ giá hiện hành đang Cũ (BR-75) → đơn không có số tham khảo. | BR-42, BR-75 | Gốc: brief (đề xuất); A-12 |

*Sau khi đặt*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-44 | Email xác nhận và My bookings hiển thị số tham khảo theo tỷ giá lúc đặt, vĩnh viễn, lấy từ đơn (BR-42), không tính lại. Đổi ngôn ngữ hoặc tiền tệ sau khi đặt không làm đổi tiền tệ và số tham khảo của đơn cũ. Ngoại lệ: xem trên UI VI thì chỉ hiển thị VND (BR-08). | Đơn đặt ở 1 USD = 26,054 VND vẫn hiện 470,300 VND : ~USD 18.05 khi tỷ giá hôm nay là 26,500 (tính lại sẽ ra ~USD 17.75). Khách đổi sang KRW → đơn cũ vẫn ~USD 18.05. | BR-08, BR-42 | Gốc: BR-P01, CR-26, US-15 |
| BR-45 | Hoàn tiền: số hoàn bằng VND là số chính; số tham khảo của số hoàn quy đổi theo bảng tỷ giá lưu trên đơn (bảng của báo giá lúc mua), với tiền tệ tham khảo của đơn, theo BR-15, và được lưu cùng bản ghi hoàn tiền. Không cần khách đồng ý. | Đơn mua ở 1 USD = 26,054 VND, hoàn 423,270 VND (giá trị mẫu) → 16.246 → 423,270 VND : ~USD 16.25, dù tỷ giá ngày hoàn là 26,500. | BR-01, BR-15, BR-42 | Gốc: BR-P02, CR-27, US-16 |
| BR-46 | Email xác nhận và vé điện tử gửi bằng ngôn ngữ UI tại thời điểm thanh toán; ngôn ngữ này được lưu trên đơn là ngôn ngữ đặt vé. Ngôn ngữ đặt vé là VI thì email, vé điện tử không có ngoại tệ. Thông báo trên app gửi theo ngôn ngữ hiện tại của khách. | Thanh toán trên UI KO, sau đó đổi app sang EN → email, vé điện tử bằng KO; thông báo app bằng EN. | BR-08 | Gốc: BR-P03 |

*Tỷ giá*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-47 | Nguồn tỷ giá cấu hình theo từng cặp tiền trên công cụ cấu hình tỷ giá; hiện có 2 nguồn: FXRatesAPI và ExchangeRate-API. Nguồn có số ưu tiên nhỏ nhất là nguồn chính, các nguồn còn lại là dự phòng; nguồn bị tắt thì bỏ qua. Mỗi cặp lấy từ nguồn ưu tiên cao nhất đang bật; nguồn lỗi hoặc thiếu cặp thì lấy nguồn kế tiếp. | Giá trị mẫu: USD/VND: 1. FXRatesAPI, 2. ExchangeRate-API. FXRatesAPI lỗi → lấy USD/VND từ ExchangeRate-API. | BR-52 | Gốc: BR-F01, CR-29 |
| BR-48 | Tỷ giá được cập nhật mỗi 2 giờ, và ngay sau khi một quy tắc tỷ giá được tạo, sửa, hoặc khi bấm làm mới trên công cụ cấu hình tỷ giá. Mỗi lần cập nhật tạo một bảng tỷ giá thống nhất, ghi nguồn và thời điểm bản tin của từng cặp. Bảng hợp lệ (BR-49) mới nhất là bảng tỷ giá hiện hành. Mọi giá trong một phiên dùng cùng một bảng tỷ giá; khi phiên kéo dài qua một lần cập nhật: TBD (Q-16). | Giá trị mẫu: lịch cập nhật 08:00, 10:00, 12:00; quy tắc USD/VND được sửa lúc 10:15 → cập nhật ngay lúc 10:15 và tạo bảng mới; lần cập nhật định kỳ kế tiếp lúc 12:00. | BR-47, BR-49, BR-52 | Gốc: BR-F01, CR-28, CR-29, US-19; quyết định 7 |
| BR-49 | Bảng tỷ giá chỉ hợp lệ khi có đủ tiền tệ chính của mọi ngôn ngữ đang bật. | Giá trị mẫu: KO đang bật, tiền tệ chính KRW; lần cập nhật không lấy được KRW/VND từ nguồn nào → bảng đó không hợp lệ, bảng hiện hành giữ nguyên. | BR-22, BR-23 | Gốc: CR-29 |
| BR-50 | Loại tỷ giá: spot. Nguồn dự phòng phải dùng cùng loại tỷ giá; nếu khác thì ghi rõ khác biệt trong bảng tỷ giá. | USD/VND lấy từ ExchangeRate-API (dự phòng) → bảng tỷ giá ghi nguồn và loại tỷ giá của cặp đó; khác spot thì ghi rõ khác biệt. | BR-47 | Gốc: BR-F02 |
| BR-51 | Nguồn tỷ giá không hiện trên giao diện chính; được công bố trong tooltip (i) cạnh disclaimer (MSG-02) và trong mục tỷ giá tham khảo của Điều khoản (MSG-15): tên nguồn, loại tỷ giá, thời điểm cập nhật của bảng tỷ giá đang dùng. | Tooltip: nguồn FXRatesAPI, loại spot, cập nhật lúc 10:00 ngày 19/10/2026. | BR-47, BR-48, BR-50 | Gốc: BR-F03 |
| BR-52 | Quy tắc tỷ giá: mỗi cặp tiền XXX/VND có một quy tắc gồm buffer %, đơn vị làm tròn (VND), biến động tối đa/ngày (%), danh sách nguồn theo thứ tự ưu tiên (BR-47) và trạng thái bật/tắt. Mọi giá trị do nhân viên vận hành tỷ giá đặt cho từng cặp trên công cụ cấu hình tỷ giá (BR-78). Brief không nêu giá trị mặc định; buffer và đơn vị làm tròn bắt buộc nhập (BR-58); biến động tối đa/ngày để trống là không giới hạn (BR-54). Tỷ giá theo quy tắc = tỷ giá gốc × (1 + buffer), làm tròn half-up tới đơn vị làm tròn của quy tắc; đơn vị làm tròn áp vào tỷ giá, tức số VND cho 1 đơn vị ngoại tệ (assumed, A-11). | Giá trị mẫu, buffer 2%: USD gốc 25,899 × 1.02 = 26,416.98, đơn vị làm tròn 1 VND → 26,417. THB gốc 772.44 × 1.02 = 787.8888, đơn vị làm tròn 0.01 VND → 787.89. | BR-47, BR-54, BR-58, BR-78 | Gốc: BR-F04, CR-34; quyết định 6 |
| BR-53 | Quy tắc tỷ giá bị tắt thì cặp tiền đó không còn trong bảng tỷ giá từ lần cập nhật ngay sau khi tắt (BR-48). Khách đang dùng tiền tệ đó chỉ thấy VND theo quy tắc tiền tệ mặc định (BR-25, CB-02). Chuyển sang ứng viên tiền tệ kế tiếp thay vì chỉ VND: TBD (Q-17). Khi cặp bị tắt là tiền tệ chính của một ngôn ngữ đang bật (BR-49): TBD (Q-14). | Giá trị mẫu: tắt quy tắc TWD/VND → khách ZH đang dùng TWD chỉ thấy VND kèm thông báo tỷ giá tạm thời không có. | BR-25, BR-48, BR-49 | Gốc: BR-F04, US-22, US-06 |
| BR-54 | Biến động tối đa/ngày: tỷ giá mới của một cặp lệch so với tỷ giá hiện hành của cặp đó quá mức biến động tối đa/ngày của quy tắc thì bị bỏ qua; giữ tỷ giá hiện hành và ghi cảnh báo. Để trống là không giới hạn. Mức lệch = giá trị tuyệt đối của (tỷ giá mới − tỷ giá hiện hành) / tỷ giá hiện hành (assumed, A-19). | Giá trị mẫu, biến động tối đa 3%, tỷ giá hiện hành 26,054: mới 27,000 → lệch 3.63% → bỏ qua, giữ 26,054. Mới 26,500 → lệch 1.71% → nhận. | BR-52, BR-55 | Gốc: CR-33 |
| BR-55 | Khi tỷ giá mới bị bỏ qua theo BR-54, có thử nguồn kế tiếp (BR-47) hay không: cài đặt Có/Không cho từng cặp tiền, do nhân viên vận hành tỷ giá chọn trên công cụ cấu hình tỷ giá (BR-78). Mặc định: brief không nêu. | Giá trị mẫu: FXRatesAPI trả 1 USD = 27,000 VND, bị bỏ qua. Có → thử ExchangeRate-API, trả 26,100 (lệch 0.18%) → dùng 26,100. Không → giữ 26,054. | BR-47, BR-54, BR-78 | Gốc: CR-33; quyết định 6 |
| BR-56 | Bảng tỷ giá hiện hành bị coi là cũ (stale) khi không tạo được bảng hợp lệ (BR-49) trong N lần cập nhật liên tiếp. N áp dụng cho cả bảng tỷ giá, do nhân viên vận hành tỷ giá đặt (BR-78); mặc định: brief không nêu. Ngày nguồn không công bố bản tin (cuối tuần, lễ) không tính là lần lỗi. Khi mọi nguồn lỗi, giữ bảng hiện hành cho tới ngưỡng này. | Giá trị mẫu: N = 3, cập nhật mỗi 2 giờ → khoảng 6 giờ không có bảng mới thì bảng hiện hành thành Cũ (BR-71). | BR-48, BR-49, BR-78 | Gốc: CR-30, US-19; quyết định 6 |
| BR-57 | Mọi thay đổi tỷ giá và quy tắc tỷ giá được ghi lại: giá trị, nguồn, thời điểm, người hoặc hệ thống thực hiện. Thời gian lưu theo NFR-02. | Giá trị mẫu: lần cập nhật 10:00 ghi USD/VND 26,054, nguồn FXRatesAPI, hệ thống thực hiện. Nhân viên sửa buffer USD/VND từ 2% sang 1.5% lúc 10:15 → ghi người sửa, 10:15, 2%, 1.5%. | BR-48, BR-52 | Gốc: NFR-02, US-19, mục 3.6.1 |
| BR-58 | Dữ liệu nhập của quy tắc tỷ giá: mã tiền bắt buộc, mã ISO 4217 3 ký tự, không sửa được sau khi tạo; tiền quy đổi sang mặc định VND, không sửa được; buffer bắt buộc, nhập theo % hoặc bps (chọn một); trạng thái Active/Inactive; đơn vị làm tròn bắt buộc; biến động tối đa/ngày tuỳ chọn; mỗi nguồn có số ưu tiên bắt buộc, không trùng, và trạng thái bật/tắt. | Mã tiền "US" (2 ký tự) bị từ chối; buffer 2% tương đương 200 bps; hai nguồn cùng ưu tiên 1 bị từ chối. | BR-11, BR-52 | Gốc: mục 3.6.1 |
| BR-59 | Mỗi cặp tiền chỉ có một quy tắc tỷ giá; tạo quy tắc cho cặp đã có thì bị từ chối. | Đã có quy tắc USD/VND → tạo thêm quy tắc USD/VND bị từ chối. | BR-52 | Gốc: US-22, mục 3.6.1 |

*Bật tắt và ra mắt*

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-60 | Currency Switch bật tắt theo từng vertical × platform (web desktop, mobile web, app); tỷ lệ traffic được tăng dần mà không cần phát hành bản mới. PO bật tắt và ramp theo phân quyền BR-77. Lúc ra mắt: chỉ vertical Bus. | Giá trị mẫu: Bus × app: 10% traffic → 50% → 100%; Bus × web desktop: tắt. | BR-77 | Gốc: US-21; quyết định 2 |
| BR-61 | Khi tắt Currency Switch cho một vertical × platform: mọi bề mặt của vertical × platform đó chuyển về chỉ hiển thị VND ngay, kể cả checkout đang dở và My bookings; số tham khảo đã lưu trên đơn được giữ và hiện lại khi bật lại; email đã gửi không đổi (assumed, A-12). Picker ngôn ngữ, tiền tệ và thông báo trong lúc tắt: TBD (Q-15). | Tắt Bus × app lúc 14:00: khách đang ở checkout trên app thấy 470,300 VND, không còn ~USD 18.05. Đơn đặt lúc 13:00 vẫn giữ ~USD 18.05 trên đơn và hiện lại khi bật lại. | BR-44, BR-60 | Gốc: US-21 (đề xuất); A-12 |
| BR-62 | Dữ liệu cũ lúc ra mắt: đơn đặt trước khi ra mắt không có số tham khảo; email, My bookings và hoàn tiền của các đơn này chỉ hiển thị VND trên mọi UI (CB-05) (assumed, A-12). | Đơn đặt một ngày trước ra mắt, xem My bookings trên UI EN sau ra mắt → chỉ 470,300 VND. | BR-44, BR-45 | Gốc: brief (đề xuất); A-12 |
| BR-63 | Checkout đang dở lúc ra mắt: báo giá tạo trước khi bật tính năng tiếp tục chỉ hiển thị VND tới khi xong đơn (assumed, A-12). | Báo giá tạo lúc 13:58, tính năng bật lúc 14:00 → checkout đó vẫn chỉ VND; đơn không có số tham khảo (BR-43). | BR-43, BR-60, BR-66 | Gốc: brief (đề xuất); A-12 |
| BR-64 | Khi một ngôn ngữ hoặc tiền tệ bị tắt: lựa chọn đã lưu không bị xoá, chỉ bị bỏ qua tới khi được bật lại; ngôn ngữ bị tắt thì dùng EN; tiền tệ bị tắt thì dùng ứng viên kế tiếp theo thứ tự ưu tiên (BR-26) (assumed, A-12). | Giá trị mẫu: khách đã lưu TH + THB; TH bị tắt → EN, tiền tệ xác định lại theo BR-26; TH bật lại → TH + THB. | BR-22, BR-26, BR-31 | Gốc: brief (đề xuất); A-12 |
| BR-65 | Trong khi Legal chưa kết luận cho trang thanh toán, email xác nhận, My bookings và số tiền hoàn (DEP-03), bốn bề mặt này chỉ hiển thị VND (assumed, A-15). | Legal chưa kết luận cho màn thanh toán → màn thanh toán chỉ hiện 470,300 VND; đơn không có số tham khảo (BR-43). | BR-43 | Gốc: UI_UX_Requirements (Legal); A-15 |

**Statuses & Transitions**

| ID | From status | Event | Condition | To status | Side-effects of this event |
|----|-------------|-------|-----------|-----------|----------------------------|
| BR-66 | — | Khách vào checkout | — | Báo giá: Đang hiệu lực | Báo giá giữ cố định: số VND; bảng tỷ giá hiện hành mới nhất (BR-48); mốc hết hiệu lực tỷ giá = lần cập nhật 2 giờ kế tiếp (BR-48); mốc hết giữ chỗ theo thời gian giữ chỗ hiện có (DEP-11). Ví dụ (giá trị mẫu): vào checkout lúc 09:40, lịch cập nhật 08:00, 10:00 → tỷ giá của báo giá hết hiệu lực lúc 10:00. Gốc: CR-22. |
| BR-67 | Báo giá: Đang hiệu lực | Tới mốc hết hiệu lực tỷ giá của báo giá | Chỗ vẫn còn được giữ và đã có bảng tỷ giá hợp lệ mới hơn (BR-49) | Báo giá: Đang hiệu lực | Báo giá chuyển sang bảng tỷ giá hiện hành mới nhất; mốc hết hiệu lực tỷ giá mới = lần cập nhật 2 giờ kế tiếp (BR-48); số VND và mốc hết giữ chỗ không đổi (BR-39); không chặn thanh toán. Gốc: BR-C04, CR-24. |
| BR-68 | Báo giá: Đang hiệu lực | Tới mốc hết hiệu lực tỷ giá của báo giá | Chỗ vẫn còn được giữ và chưa có bảng tỷ giá hợp lệ mới (BR-49) | Báo giá: Đang hiệu lực | Báo giá giữ tỷ giá hiện có cho tới khi bảng tỷ giá hiện hành thành Cũ (BR-71); không chặn thanh toán (assumed, A-12). Gốc: BR-C04, CR-24 (đề xuất). |
| BR-69 | Báo giá: Đang hiệu lực | Hết thời gian giữ chỗ (DEP-11) | — | Báo giá: Hết hạn | — (xem BR-74). Gốc: CR-24, US-14. |
| BR-70 | Báo giá: Đang hiệu lực | Khách thanh toán thành công | — | Báo giá: Đã thành đơn | Đơn lưu số VND của báo giá và ngôn ngữ đặt vé (BR-46). Nếu BR-43 cho phép, đơn lưu thêm: tiền tệ tham khảo, số tham khảo tính lại theo BR-42, tỷ giá và nguồn tỷ giá lấy từ bảng tỷ giá của báo giá, nhóm hiển thị Browse/Pay theo chế độ BR-06, phiên bản, ngôn ngữ và thời điểm disclaimer (MSG-01) được hiển thị cho khách. Gốc: CR-25, US-17. |
| BR-71 | Bảng tỷ giá hiện hành: Hợp lệ | Một lần cập nhật không tạo được bảng tỷ giá hợp lệ (BR-49) | Đã đủ ngưỡng N lần liên tiếp (BR-56) | Bảng tỷ giá hiện hành: Cũ (stale) | — (xem BR-75). Gốc: CR-30, CR-31. |
| BR-72 | Bảng tỷ giá hiện hành: Hợp lệ | Bật công tắc tắt khẩn cấp (người có quyền theo BR-77) | — | Bảng tỷ giá hiện hành: Cũ (stale) | — (xem BR-75). Cách vận hành: Q-10. Gốc: CR-31. |
| BR-73 | Bảng tỷ giá hiện hành: Cũ (stale) | Một lần cập nhật tạo được bảng tỷ giá hợp lệ (BR-49) | Công tắc tắt khẩn cấp không bật (BR-72) | Bảng tỷ giá hiện hành: Hợp lệ | Bảng mới thành bảng tỷ giá hiện hành (BR-48). Gốc: CR-30. |

**On Entering a Status**

| ID | Status | Side-effects |
|----|--------|--------------|
| BR-74 | Báo giá: Hết hạn | Chỗ được nhả; báo giá không còn dùng được; khách phải chọn lại chuyến để có báo giá mới (BR-66). Gốc: CR-24, US-14. |
| BR-75 | Bảng tỷ giá hiện hành: Cũ (stale) | Mọi bề mặt chỉ hiển thị VND, không dùng tỷ giá của bảng cũ, kể cả báo giá đang mở (BR-68), kèm MSG-06 (CB-02). Đơn thanh toán trong thời gian này không có số tham khảo (BR-43). Gốc: BR-D09, CR-31. |

**Roles & Permissions**

| ID | Action | Who may act |
|----|--------|-------------|
| BR-76 | Bật, tắt ngôn ngữ và tiền tệ; sửa phạm vi tiền tệ của ngôn ngữ và bảng quốc gia → tiền tệ (BR-22, BR-23) | Theo phân quyền hiện có của hệ thống (DEP-15); PRD này không định nghĩa lại. Gốc: US-20. |
| BR-77 | Bật tắt và ramp Currency Switch theo vertical × platform (BR-60); bật, tắt công tắc tắt khẩn cấp (BR-72) | Theo phân quyền hiện có của hệ thống (DEP-15); PRD này không định nghĩa lại. Gốc: US-21, CR-31. |
| BR-78 | Tạo, sửa, bật tắt quy tắc tỷ giá và từng nguồn; đặt các giá trị của quy tắc và ngưỡng bảng cũ; làm mới tỷ giá trên công cụ (BR-14, BR-48, BR-52 đến BR-59) | Theo phân quyền hiện có của hệ thống (DEP-15); PRD này không định nghĩa lại. Gốc: US-22. |
| BR-79 | Đổi chế độ thứ bậc hiển thị (BR-06) | Theo phân quyền hiện có của hệ thống (DEP-15); PRD này không định nghĩa lại. Gốc: CR-04. |

## 4. Messages

Placeholder số tiền chỉ chứa số đã định dạng theo BR-09, BR-10, BR-12, không kèm mã tiền; mã tiền nằm trong câu copy để tránh lặp như "VND VND 470,300". Copy EN giữ nguyên tiếng Anh; bản dịch theo ngôn ngữ UI do Đội dịch thuật cung cấp (DEP-05) và Legal duyệt theo quy trình riêng (DEP-03).

| ID | Channel | Message | Rules |
|----|---------|---------|-------|
| MSG-01 | Màn hình, cạnh bảng giá, một lần mỗi trang (disclaimer) | "Prices in {mã tiền tệ} are for reference only. You will be charged in VND." | BR-01, BR-05 |
| MSG-02 | Màn hình, tooltip (i) cạnh disclaimer | "Reference rates: {nguồn tỷ giá}, {loại tỷ giá (BR-50)}, updated {thời điểm cập nhật của bảng tỷ giá}. See Terms for details." | BR-47, BR-48, BR-50, BR-51 |
| MSG-03 | Màn hình, picker tiền tệ chỉ đọc (ngôn ngữ chỉ có 1 tiền tệ) | "Prices in {mã tiền tệ}" | BR-23 |
| MSG-04 | Màn hình, picker tiền tệ | (proposed copy) Ý: cho biết đây là tiền hiển thị, không phải tiền thanh toán. Đề xuất: "Display currency only. You will be charged in VND." | BR-01, BR-23 |
| MSG-05 | Màn hình, picker tiền tệ, tên hai nhóm | (proposed copy) "Suggested" / "All currencies" | BR-27 |
| MSG-06 | Màn hình, cạnh bảng giá, một lần mỗi trang | "Reference prices in {mã tiền tệ} are temporarily unavailable. Prices are shown in VND." | BR-25, BR-53, BR-75 |
| MSG-07 | Màn hình, checkout, ngay dưới tổng tiền | "You'll pay in VND" | BR-01, BR-06 |
| MSG-08 | Màn hình, checkout, hộp Payment Notice bản đầy đủ | "Payment Notice: You will be charged exactly {số tiền VND} VND. The converted amount (~{số tham khảo} {mã tiền tệ}) is for reference only. Your issuing bank may apply its own exchange rate and international transaction fees." Thứ tự "{số tham khảo} {mã tiền tệ}" khác vị trí mã ngoại tệ của BR-12: Q-13. | BR-01, BR-02, BR-12, BR-15, BR-39, BR-41 |
| MSG-09 | Màn hình, màn thanh toán, Payment Notice rút gọn một dòng ngay trên nút thanh toán | "You will be charged exactly {số tiền VND} VND. {mã tiền tệ} amounts are for reference only." | BR-01, BR-39, BR-41 |
| MSG-10 | Màn hình, màn thanh toán, nhãn nút thanh toán | "Pay {số tiền VND} VND" | BR-01, BR-12, BR-39 |
| MSG-11 | Màn hình, màn thanh toán, một dòng ngay dưới nút thanh toán | "By clicking Pay, you agree that your transaction will be processed in VND." | BR-01 |
| MSG-12 | Màn hình, toast | "Reference rate updated to the bank's latest session." | BR-67 |
| MSG-13 | Màn hình, trang kết quả tìm kiếm sau khi hết giữ chỗ | "Your seat hold has expired. Please select your trip again." | BR-69, BR-74 |
| MSG-14 | Màn hình, cạnh số tiền hoàn | "You will be refunded {số tiền hoàn VND} VND. The {mã tiền tệ} amount is based on the reference rate at booking. The amount credited to your card depends on your bank's exchange rate on the refund date." | BR-01, BR-45 |
| MSG-15 | Điều khoản (T&C), mục tỷ giá tham khảo | Nội dung do Legal soạn (DEP-03), gồm: nguồn chính, nguồn dự phòng, loại tỷ giá, tần suất cập nhật, cách làm tròn. | BR-10, BR-47, BR-48, BR-50, BR-51, BR-52 |
| MSG-16 | Màn hình, bước nhập thông tin hành khách, gợi ý ở ô tên (UI ngoại ngữ) | "Enter your name in Latin letters, as shown on your passport." | — |
| MSG-17 | Màn hình, bước nhập thông tin hành khách, lỗi inline dưới ô tên | Thông báo lỗi hiện có của hệ thống khi tên hành khách có ký tự không hợp lệ, hiển thị bằng ngôn ngữ UI (copy hiện có, DEP-10). | — |
| MSG-18 | Màn hình, search widget, không có kết quả | "No matching places. Try another name or check the spelling." (copy đề xuất trong brief) | — |
| MSG-19 | Back office, thông tin tiền tệ của đơn | "không có số tham khảo" | BR-43, BR-62, BR-65 |
| MSG-20 | VEX-CONFIG, form tạo quy tắc tỷ giá | "rule đã tồn tại", kèm link sang quy tắc cũ của cặp tiền. | BR-59 |
| MSG-21 | VEX-CONFIG, form tạo, sửa quy tắc tỷ giá, lỗi inline dưới trường không hợp lệ | (proposed copy) Ý: cho biết trường nào không hợp lệ và trường đó phải nhập theo yêu cầu nào. Đề xuất: "{tên trường}: {yêu cầu của trường (BR-58)}" | BR-58 |

## 5. Common Behaviors

| ID | Situation | What the user sees / what happens | Rules & Messages |
|----|-----------|-----------------------------------|------------------|
| CB-01 | Bảng tỷ giá đang tải | Ô giá hiện khung chờ (skeleton) cho tới khi có bảng tỷ giá; không ô nào hiện ngoại tệ mà thiếu VND (BR-07). | BR-07, BR-48 |
| CB-02 | Số tham khảo tạm thời không có: bảng tỷ giá hiện hành đang Cũ, kể cả khi bật công tắc tắt khẩn cấp (BR-71, BR-72, BR-75); tiền tệ của khách không có trong bảng tỷ giá hiện hành (BR-53); không có ứng viên tiền tệ hợp lệ (BR-25) | Mọi giá chỉ hiển thị VND, không có số tham khảo; MSG-06 hiện một lần mỗi trang, cạnh bảng giá. Khách vẫn tìm chuyến, đặt vé và thanh toán bằng VND như bình thường (BR-01). | BR-01, BR-25, BR-53, BR-71, BR-72, BR-75; MSG-06 |
| CB-03 | Currency Switch đang tắt cho vertical × platform khách đang dùng (BR-60, BR-61) | Mọi bề mặt chỉ hiển thị VND, không có số tham khảo, kể cả checkout đang dở và My bookings; email đã gửi không đổi (BR-61). Picker và thông báo trong lúc tắt: TBD (Q-15). | BR-60, BR-61 |
| CB-04 | Tiền tệ hiện hành là VND: UI VI, hoặc khách chọn VND (BR-08) | Mọi giá chỉ hiển thị VND, không có số quy đổi (BR-08); trên UI VI không có picker tiền tệ (BR-23). | BR-08, BR-23 |
| CB-05 | Đơn không có số tham khảo: đơn đặt trước khi ra mắt (BR-62), màn thanh toán không hiển thị số tham khảo (BR-43), hoặc bề mặt chờ kết luận của Legal (BR-65) | Email xác nhận, My bookings và số tiền hoàn của đơn chỉ hiển thị VND trên mọi UI; back office hiển thị MSG-19 ở phần thông tin tiền tệ của đơn. | BR-43, BR-44, BR-45, BR-62, BR-65; MSG-19 |

## 6. Referenced Items

**Success Metrics**

| ID | Type | Metric | How it is measured | Baseline | Target | Owner |
|----|------|--------|--------------------|----------|--------|-------|
| SM-01 | Primary | Tỷ lệ hoàn thành đơn ở các user dùng page ngoại ngữ (North-star) | Số đơn thanh toán thành công chia cho số phiên có xem kết quả tìm kiếm trên UI ngoại ngữ, vertical Bus, tính theo tuần | Trung bình 4 tuần trước khi bật tính năng cho Bus | Tăng so với baseline; mức cụ thể TBD (Q-01) | PO |
| SM-02 | Secondary | Conversion UI ngoại ngữ | Tỷ lệ chuyển giữa các bước trên UI ngoại ngữ, vertical Bus, theo tuần: kết quả tìm kiếm → chọn chuyến và chỗ → checkout → thanh toán thành công | Trung bình 4 tuần trước khi bật tính năng cho Bus | Tăng so với baseline ở từng bước; mức cụ thể TBD (Q-01) | PO |
| SM-03 | Guardrail | Conversion UI VI | Số đơn thanh toán thành công chia cho số phiên có xem kết quả tìm kiếm trên UI tiếng Việt, vertical Bus, tính theo tuần | Trung bình 4 tuần trước khi bật tính năng cho Bus | Không giảm | PO |
| SM-04 | Guardrail | Ticket CSKH "giá khác số bị trừ" | Số ticket CSKH phân loại "giá khác số bị trừ" trên 1,000 đơn UI ngoại ngữ, theo tuần | Trung bình 4 tuần trước khi bật tính năng cho Bus | Không tăng | Trưởng nhóm CSKH |
| SM-05 | Guardrail | Tỷ lệ hoàn và chargeback đơn UI ngoại ngữ | Số đơn UI ngoại ngữ bị hoàn tiền hoặc chargeback chia cho số đơn UI ngoại ngữ thanh toán thành công, theo tháng | Trung bình 3 tháng trước khi bật tính năng cho Bus | Không tăng | Finance |

**Quality Targets**

| ID | Expectation | Target | Why it matters |
|----|-------------|--------|----------------|
| NFR-01 | Khi khách đổi tiền tệ ở trang kết quả tìm kiếm, toàn bộ giá trên trang cập nhật theo tiền tệ mới | Dưới 200 ms | Khách so sánh giá ngay khi đổi tiền tệ, không phải chờ |
| NFR-02 | Lịch sử thay đổi tỷ giá và quy tắc tỷ giá (BR-57) được giữ lại | Tối thiểu 24 tháng | Đủ bằng chứng cho khiếu nại, hoàn tiền, chargeback và kiểm tra nội bộ |
| NFR-03 | Số tham khảo của cùng một số tiền giống hệt nhau ở mọi nơi hiển thị: web, app, email, back office | 0 lệch | Số tham khảo khác nhau giữa các nơi tạo khiếu nại "giá khác số bị trừ" (SM-04) |
| NFR-04 | Nền tảng hỗ trợ | Web desktop, mobile web, app | Khách quốc tế đặt vé trên cả ba platform |

**Dependencies**

| ID | Depends on | What we need from it | If it is unavailable | Owner |
|----|------------|----------------------|----------------------|-------|
| DEP-01 | Nguồn tỷ giá FXRatesAPI và ExchangeRate-API | Tỷ giá spot cho từng cặp tiền XXX/VND (BR-47, BR-50) | Lấy từ nguồn kế tiếp (BR-47); mọi nguồn lỗi thì giữ bảng hiện hành tới ngưỡng BR-56, sau đó chỉ hiển thị VND (BR-75, CB-02) | Nhân viên vận hành tỷ giá |
| DEP-02 | Công cụ cấu hình nội bộ VEX-CONFIG | Màn "Cấu hình tỷ giá" để quản lý quy tắc tỷ giá (SCR-16, SCR-17; BR-52 đến BR-59) | Không tạo, sửa được quy tắc trong thời gian đó; nếu vì vậy không tạo được bảng tỷ giá hợp lệ thì áp dụng ngưỡng bảng cũ (BR-56, BR-75) | Dev / Tech Lead |
| DEP-03 | Legal | Kết luận cho trang thanh toán, email xác nhận, My bookings, số tiền hoàn; soạn mục tỷ giá tham khảo trong T&C (MSG-15); duyệt copy theo quy trình riêng của Legal | Bốn bề mặt chờ kết luận chỉ hiển thị VND (BR-65, CB-05) | Legal |
| DEP-04 | Design | Thể hiện hai chế độ thứ bậc hiển thị (BR-06) và vị trí mã tiền (BR-12); thiết kế cho các SCR | Bề mặt chưa có thiết kế thì chưa build được; không có hành vi thay thế | Design |
| DEP-05 | Đội dịch thuật | Bản dịch cho từng ngôn ngữ được bật (BR-35) và bản dịch Payment Notice được duyệt (BR-41) | Ngôn ngữ chưa có bản dịch thì chưa bật được (BR-35); Payment Notice chưa duyệt thì hiển thị bản EN (BR-41) | Đội dịch thuật |
| DEP-06 | Back office CSKH | Hiển thị thông tin tiền tệ của đơn (SCR-15; BR-70) | CSKH xử lý ticket theo quy trình hiện tại, không có bằng chứng tiền tệ của đơn; khách không bị ảnh hưởng | Trưởng nhóm CSKH |
| DEP-07 | Kế toán và Finance | Hoá đơn VAT và báo cáo doanh thu giữ VND như hiện tại (BR-03, BR-04) | Không thay đổi: hoá đơn và báo cáo vẫn bằng VND (BR-03, BR-04) | Finance |
| DEP-08 | SEO | Đường dẫn theo ngôn ngữ cho mỗi ngôn ngữ mới; công cụ tìm kiếm nhận đúng trang theo ngôn ngữ và giá VND (BR-28) | Trang ngôn ngữ mới chưa được công cụ tìm kiếm ghi nhận; khách vẫn dùng được trang (BR-28) | SEO |
| DEP-09 | Marketing và affiliate | Link có chỉ định ngôn ngữ và tiền tệ (BR-26, BR-34) | Link không chỉ định thì ngôn ngữ, tiền tệ theo các ứng viên còn lại của BR-26 | Marketing |
| DEP-10 | Hạng mục "Đăng ký" và bước nhập thông tin hành khách hiện có | Quy tắc ký tự hợp lệ của tên hành khách và thông báo lỗi hiện có (MSG-17); gợi ý nhập tên Latin (MSG-16) | Không chặn ngày ra mắt; ô tên hoạt động như hiện tại | PO |
| DEP-11 | Tính năng giữ chỗ hiện có | Thời gian giữ chỗ của hệ thống, dùng cho mốc hết giữ chỗ của báo giá (BR-66, BR-69) | Theo hành vi giữ chỗ hiện có; báo giá hết hạn theo BR-69, BR-74 | Dev / Tech Lead |
| DEP-12 | Email xác nhận, vé điện tử và thông báo trên app | Gửi theo ngôn ngữ đặt vé (BR-46) và hiển thị số tham khảo của đơn (BR-44) | Theo hành vi hiện có của kênh gửi; số tham khảo vẫn xem được trên My bookings (BR-44) | Dev / Tech Lead |
| DEP-13 | BRD Currency Switch (Multi-currency Display & Settlement) và Timeline Dev | Tài liệu tham chiếu cho phạm vi và kế hoạch | BRD chưa được cung cấp; Pack dựa trên PRD v0.1 (A-01) | PO |
| DEP-14 | BU | Cấu hình danh sách ngôn ngữ, tiền tệ, phạm vi tiền tệ của ngôn ngữ và bảng quốc gia → tiền tệ (BR-22, BR-23) | Ngôn ngữ chưa bật thì dùng EN (BR-22); không có tiền tệ hợp lệ thì chỉ hiển thị VND (BR-25, CB-02) | BU |
| DEP-15 | Phân quyền hiện có của hệ thống | Quyết định ai được thực hiện các thao tác BR-76 đến BR-79 | Các thao tác BR-76 đến BR-79 không thực hiện được; cấu hình đang có giữ nguyên | Dev / Tech Lead |

**Screens**

| ID | Screen | Purpose | Design |
|----|--------|---------|--------|
| SCR-01 | Trang kết quả tìm kiếm | Xem, lọc và chọn chuyến; gồm lịch giá theo ngày, bộ lọc và thanh trượt giá, nhãn giảm giá; giá hiển thị kép (BR-05) | |
| SCR-02 | Trang tìm nhà xe | Tìm nhà xe; giá hiển thị kép (BR-05) | |
| SCR-03 | Trang chi tiết chuyến | Xem chi tiết chuyến và điểm đón trả; giá theo đơn giá (BR-19) | |
| SCR-04 | Sơ đồ ghế | Chọn ghế, giường; giá từng ghế, giường theo đơn giá (BR-19) | |
| SCR-05 | Checkout | Breakdown phí (phí dịch vụ, phí thanh toán, bảo hiểm, dịch vụ thêm), voucher và khuyến mãi, total; thông báo thanh toán bằng VND | |
| SCR-06 | Bước nhập thông tin hành khách | Nhập thông tin hành khách; bước cuối còn đổi được ngôn ngữ, tiền tệ (BR-40) | |
| SCR-07 | Màn thanh toán | Thanh toán bằng VND; Payment Notice rút gọn, nút thanh toán | |
| SCR-08 | Email xác nhận và vé điện tử | Xác nhận đơn theo ngôn ngữ đặt vé (BR-46), kèm số tham khảo lúc đặt (BR-44) | |
| SCR-09 | My bookings | Xem đơn đã đặt với số tham khảo lúc đặt (BR-44) | |
| SCR-10 | Số tiền hoàn (thông tin hoàn tiền của đơn) | Xem số tiền hoàn bằng VND kèm số tham khảo theo tỷ giá ngày mua (BR-45) | |
| SCR-11 | Trang SEO landing | Trang đích từ công cụ tìm kiếm; giá hiển thị kép (BR-05) | |
| SCR-12 | Picker ngôn ngữ (web và app) | Chọn ngôn ngữ UI | |
| SCR-13 | Picker tiền tệ (web và app) | Chọn tiền tệ tham khảo trong phạm vi của ngôn ngữ (BR-23) | |
| SCR-14 | Search widget (web desktop, mobile web, app) | Tìm chuyến theo ngôn ngữ UI, địa danh không dấu (BR-37) | |
| SCR-15 | Back office đơn hàng (CSKH) | Xem thông tin tiền tệ của từng đơn | |
| SCR-16 | VEX-CONFIG - Cấu hình tỷ giá: danh sách quy tắc (Home / Fx Conversion Rule) | Xem, lọc quy tắc tỷ giá; làm mới tỷ giá; mở form thêm quy tắc | |
| SCR-17 | VEX-CONFIG - Cấu hình tỷ giá: form tạo, sửa quy tắc | Tạo, sửa quy tắc tỷ giá và nguồn của một cặp tiền | |
| SCR-18 | Trang tạo bản dịch cho ngôn ngữ mới (web và app) (proposed) | Tạo bản dịch của ngôn ngữ mới từ bản EN (en-US) | |
| SCR-19 | Trang xem trước bản dịch (web và app) (proposed) | Xem trước UI với bản dịch mới trước khi bật ngôn ngữ | |
| SCR-20 | Điều khoản (T&C) - mục tỷ giá tham khảo | Công bố nguồn, loại tỷ giá, tần suất cập nhật, cách làm tròn (BR-51, MSG-15) | |

## 7. Epics & User Stories

### Epic 1 - Nền tảng

**Serves:** JTBD-01, JTBD-03

#### US-01 - Số tiền hiển thị theo một quy ước thống nhất

Là khách đặt vé trên Vexere,
tôi muốn mọi số tiền trên mọi trang và mọi platform được viết theo cùng một quy ước của ngôn ngữ tôi đang dùng,
để tôi không đọc nhầm giá.

**Priority:** Must
**Screens:** SCR-01, SCR-02, SCR-03, SCR-04, SCR-05, SCR-07, SCR-08, SCR-09, SCR-10, SCR-11, SCR-15
**Common behaviors:** none
**Rules applied (PRD Currency Switch):** BR-09, BR-10, BR-11, BR-12

**Acceptance Criteria**

- AC1 (Happy) Done when: Trên mọi màn hình của story và mọi platform (NFR-04), mỗi số tiền hiển thị kèm mã ISO của tiền tệ, không số tiền nào dùng ký hiệu tiền tệ (BR-11).
- AC2 (Happy) Done when: Mỗi số VND được viết theo cách viết số của ngôn ngữ UI đang dùng, với mã VND đứng sau số (BR-12).
- AC3 (Happy) Done when: Mỗi số ngoại tệ hiển thị có mã tiền đứng trước số (BR-12), trừ trường hợp đang chờ kết luận ở Q-13.
- AC4 (Happy) Done when: Trong cùng một ngôn ngữ UI, cùng một số VND được viết giống hệt nhau trên mọi màn hình của story và mọi platform (BR-12, NFR-04).
- AC5 (Happy) Done when: Mỗi số tiền hiển thị đúng số lẻ của tiền tệ đó theo bảng số lẻ của Vexere (BR-09).
- AC6 (Alternative) Done when: Nếu tiền tệ tham khảo không có trong bảng số lẻ của Vexere (BR-09), số tham khảo hiển thị theo số lẻ mà BR-09 quy định cho tiền tệ ngoài bảng.
- AC7 (Happy) Done when: Nếu số quy đổi có nhiều chữ số thập phân hơn số lẻ của tiền tệ (BR-09), số hiển thị được làm tròn theo quy tắc làm tròn chung (BR-10).
- AC8 (Happy) Done when: Số tham khảo của cùng một số tiền hiển thị giống hệt nhau ở mọi nơi hiển thị (NFR-03).

**INVEST Check:** I / N / V / E / S / T — S chưa đạt: quy ước áp dụng cho 11 màn hình trên 3 platform, khó xong trong một sprint; nên tách theo platform hoặc theo nhóm màn hình khi lập kế hoạch.

#### US-02 - Địa danh không dấu trên UI ngoại ngữ

Là khách inbound,
tôi muốn đọc tên bến xe, trạm dừng, điểm đón trả ở dạng không dấu,
để tôi đọc và gõ được tên điểm đón mà không cần bàn phím tiếng Việt.

**Priority:** Must
**Screens:** SCR-01, SCR-03, SCR-05, SCR-08, SCR-09, SCR-11, SCR-14
**Common behaviors:** none
**Rules applied (PRD Currency Switch):** BR-37, BR-38

**Acceptance Criteria**

- AC1 (Happy) Done when: Trong khi khách dùng UI ngoại ngữ (BR-37), mọi địa danh Bus hiển thị dạng không dấu trên mọi màn hình có địa danh, gồm SCR-01, SCR-03, SCR-05, SCR-09, SCR-11 và SCR-14.
- AC2 (Happy) Done when: Nếu email xác nhận và vé điện tử (SCR-08) được gửi bằng một ngoại ngữ (BR-37), mọi địa danh Bus trong đó hiển thị dạng không dấu.
- AC3 (Happy) Done when: Tên không dấu của mỗi địa danh đúng bằng kết quả chuẩn hoá tên tiếng Việt của địa danh đó theo BR-38.
- AC4 (Happy) Done when: Cùng một địa danh hiển thị cùng một tên không dấu trên mọi ngôn ngữ ngoại ngữ đang bật và mọi platform (BR-37, NFR-04).
- AC5 (Alternative) Done when: Nếu khách dùng một ngôn ngữ ngoại ngữ được bật sau ngày ra mắt (BR-37), địa danh Bus hiển thị cùng tên không dấu như trên các ngôn ngữ ngoại ngữ khác.
- AC6 (Alternative) Done when: Trong khi khách dùng UI VI (ngoài phạm vi BR-37), địa danh vẫn hiển thị bằng tiếng Việt có dấu như hiện tại.

**INVEST Check:** I / N / V / E / S / T

#### US-03 - Search widget đa ngôn ngữ

Là khách inbound,
tôi muốn tìm chuyến bằng ngôn ngữ của mình,
để tôi bắt đầu đặt vé mà không phải đọc tiếng Việt.

**Priority:** Must
**Screens:** SCR-14, SCR-01
**Common behaviors:** none
**Rules applied (PRD Currency Switch):** BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-26, BR-28, BR-29, BR-30, BR-31, BR-32, BR-33, BR-34, BR-37, BR-38, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-66, BR-68, BR-71, BR-75, BR-76, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Trên mọi platform (NFR-04), nhãn, chữ gợi ý trong ô nhập và thông báo lỗi của search widget (SCR-14) hiển thị bằng ngôn ngữ UI khách đang dùng.
- AC2 (Happy) Done when: Khi khách gõ tên một địa danh Bus bằng chữ Latin không dấu, danh sách gợi ý hiện địa danh đó ở dạng không dấu (BR-37).
- AC3 (Happy) Done when: Sau khi khách chọn một gợi ý, ô điểm đi hoặc điểm đến hiển thị tên không dấu của địa danh đã chọn (BR-37).
- AC4 (Happy) Done when: Khi khách bấm tìm, trang kết quả tìm kiếm (SCR-01) mở bằng đúng ngôn ngữ UI khách đang dùng (trên web, theo ngôn ngữ trong đường dẫn, BR-28).
- AC5 (Alternative) Done when: Nếu một ngôn ngữ ngoại ngữ được bật sau ngày ra mắt (BR-22), nhãn, chữ gợi ý trong ô nhập và thông báo lỗi của search widget hiển thị bằng ngôn ngữ đó ngay khi ngôn ngữ được bật.
- AC6 (Error) Done when: Nếu không có địa danh nào khớp với nội dung khách gõ, danh sách gợi ý hiện MSG-18 bằng ngôn ngữ UI.

**INVEST Check:** I / N / V / E / S / T — I chưa đạt: gợi ý và tên điểm đã chọn dùng địa danh không dấu của US-02 (BR-37); nên làm cùng hoặc sau US-02.

#### US-04 - UI ngoại ngữ không còn nội dung tiếng Việt của Vexere — No longer applies: ngoài phạm vi đợt này (Phase 2)

#### US-23 - Gợi ý nhập tên hành khách bằng chữ Latin

Là khách inbound,
tôi muốn biết phải nhập tên hành khách bằng chữ Latin như trên hộ chiếu,
để tôi không bị báo lỗi khi nhập tên.

**Priority:** Should
**Screens:** SCR-06
**Common behaviors:** none
**Rules applied (PRD Currency Switch):** none

**Acceptance Criteria**

- AC1 (Happy) Done when: Trong khi khách dùng UI ngoại ngữ, mỗi ô tên hành khách ở bước nhập thông tin hành khách (SCR-06) luôn hiện MSG-16 bằng ngôn ngữ UI, có sẵn trước khi khách bắt đầu nhập.
- AC2 (Error) Done when: Nếu tên hành khách có ký tự không hợp lệ theo quy tắc ký tự hiện có của hệ thống (DEP-10), lỗi inline dưới ô tên hiện MSG-17 bằng ngôn ngữ UI.
- AC3 (Alternative) Done when: Trong khi khách dùng UI VI, ô tên hành khách không hiện MSG-16 và hoạt động như hiện tại.

**INVEST Check:** I / N / V / E / S / T

### Epic 2 - Chọn ngôn ngữ và tiền tệ

**Serves:** JTBD-01, JTBD-03, JTBD-04, JTBD-05

#### US-05 - Chọn ngôn ngữ

Là khách inbound,
tôi muốn chọn ngôn ngữ hiển thị của Vexere,
để tôi đặt vé bằng ngôn ngữ mình đọc được.

**Priority:** Must
**Screens:** SCR-05, SCR-06, SCR-12
**Common behaviors:** CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-24, BR-25, BR-26, BR-28, BR-29, BR-30, BR-31, BR-32, BR-33, BR-34, BR-39, BR-40, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-64, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Trên mọi platform (NFR-04), picker ngôn ngữ chỉ liệt kê các ngôn ngữ đang bật (BR-22).
- AC2 (Happy) Done when: Picker ngôn ngữ hiển thị ngôn ngữ hiện hành, xác định theo thứ tự ưu tiên (BR-26), là ngôn ngữ đang được chọn.
- AC3 (Happy) Done when: Sau khi khách chọn một ngôn ngữ khác trên picker, giao diện Vexere hiển thị bằng ngôn ngữ vừa chọn.
- AC4 (Happy) Done when: Trên web, sau khi khách chọn một ngôn ngữ khác, trang chuyển tới đường dẫn của ngôn ngữ vừa chọn (BR-28).
- AC5 (Happy) Done when: Sau khi khách đổi ngôn ngữ, giá tham khảo hiển thị bằng tiền tệ được xác định lại trong phạm vi tiền tệ của ngôn ngữ mới (BR-24).
- AC6 (Alternative) Done when: Nếu khách đổi ngôn ngữ trong checkout, trước màn thanh toán (BR-40), số VND của báo giá không đổi (BR-39).
- AC7 (Error) Done when: Nếu ngôn ngữ đã lưu của khách đang bị tắt (BR-64), Vexere hiển thị bằng ngôn ngữ dự phòng của BR-64.
- AC8 (Happy) Done when: Hệ thống ghi nhận ngôn ngữ UI của từng phiên để đo SM-01, SM-02 và SM-03.

**INVEST Check:** I / N / V / E / S / T

#### US-06 - Tiền tệ theo ngôn ngữ

Là khách inbound,
tôi muốn thấy giá tham khảo bằng tiền tệ gắn với ngôn ngữ tôi đọc,
để tôi không phải tự cấu hình thêm.

**Priority:** Must
**Screens:** SCR-01, SCR-05, SCR-06, SCR-13
**Common behaviors:** CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-26, BR-27, BR-29, BR-30, BR-31, BR-32, BR-33, BR-34, BR-39, BR-40, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-64, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Nếu khách chưa có tiền tệ hợp lệ nào ở các bước đứng trước bước mặc định của thứ tự ưu tiên (BR-26), giá tham khảo hiển thị bằng tiền tệ mặc định theo ngôn ngữ hiện hành (BR-25).
- AC2 (Happy) Done when: Trên mọi platform (NFR-04), picker tiền tệ chỉ liệt kê danh sách tiền tệ khách chọn được của ngôn ngữ hiện hành (BR-23).
- AC3 (Happy) Done when: Ở mọi ngôn ngữ UI có picker tiền tệ, picker hiển thị MSG-04.
- AC4 (Happy) Done when: Trong khi ngôn ngữ hiện hành thuộc diện có nhóm tiền tệ gợi ý (BR-27), picker tiền tệ hiện nhóm tiền tệ gợi ý trước nhóm tất cả tiền tệ, theo thành phần và thứ tự của BR-27, với tên nhóm là MSG-05.
- AC5 (Happy) Done when: Sau khi khách chọn một tiền tệ khác trên picker, mọi giá trên trang hiển thị số tham khảo bằng tiền tệ vừa chọn.
- AC6 (Happy) Done when: Ở trang kết quả tìm kiếm, sau khi khách đổi tiền tệ, toàn bộ giá trên trang cập nhật theo tiền tệ mới trong thời gian của NFR-01.
- AC7 (Alternative) Done when: Nếu ngôn ngữ hiện hành chỉ khai báo một tiền tệ (BR-23), picker tiền tệ ở dạng chỉ đọc và hiển thị MSG-03.
- AC8 (Alternative) Done when: Nếu khách đổi tiền tệ trong checkout, trước màn thanh toán (BR-40), số VND của báo giá không đổi (BR-39).
- AC9 (Alternative) Done when: Nếu khách đổi tiền tệ trong checkout, trước màn thanh toán (BR-40), số tham khảo theo tiền tệ mới được quy đổi bằng bảng tỷ giá của báo giá (BR-39).
- AC10 (Error) Done when: Nếu tiền tệ đã lưu của khách đang bị tắt (BR-64), giá tham khảo hiển thị bằng tiền tệ của ứng viên kế tiếp theo thứ tự ưu tiên (BR-26).

**INVEST Check:** I / N / V / E / S (chưa đạt) / T
- S: picker tiền tệ trên ba platform cùng nhóm tiền tệ gợi ý (BR-27) và NFR-01 có thể vượt một sprint; nếu vậy, tách nhóm tiền tệ gợi ý thành story riêng.

#### US-07 - Lưu lại các lựa chọn

Là khách quay lại Vexere,
tôi muốn ngôn ngữ, tiền tệ đã chọn được giữ qua các phiên, các thiết bị,
để tôi không phải chọn lại.

**Priority:** Should
**Screens:** SCR-12, SCR-13
**Common behaviors:** CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-26, BR-29, BR-30, BR-31, BR-32, BR-33, BR-34, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-64, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Sau khi guest đổi ngôn ngữ hoặc tiền tệ trên picker, lần sau mở Vexere trên cùng thiết bị, Vexere dùng đúng giá trị vừa chọn (BR-31).
- AC2 (Happy) Done when: Sau khi khách đã đăng nhập đổi ngôn ngữ hoặc tiền tệ trên picker, khi đăng nhập trên một thiết bị khác, khách thấy đúng giá trị vừa chọn (BR-31, BR-32).
- AC3 (Alternative) Done when: Nếu ngôn ngữ hoặc tiền tệ trên thiết bị khác với trên hồ sơ lúc khách đăng nhập, Vexere dùng giá trị thắng theo BR-32.
- AC4 (Alternative) Done when: Nếu lựa chọn trên thiết bị thắng khi khách đăng nhập (BR-32), lần sau khách đăng nhập trên thiết bị khác cũng thấy lựa chọn đó.
- AC5 (Alternative) Done when: Nếu khách chuyển sang ngôn ngữ có phạm vi tiền tệ không chứa tiền tệ đã lưu rồi quay lại ngôn ngữ có phạm vi chứa nó (BR-33), giá tham khảo hiển thị lại bằng tiền tệ đã lưu.
- AC6 (Error) Done when: Nếu ngôn ngữ hoặc tiền tệ đã lưu đang bị tắt (BR-64), lựa chọn đó không bị mất: khi được bật lại, Vexere dùng lại đúng lựa chọn đã lưu.

**INVEST Check:** I (chưa đạt) / N / V / E / S / T
- I: cần picker của US-05 và US-06 để khách có lựa chọn chủ động; làm sau hai story đó.

#### US-08 - Ngôn ngữ và tiền tệ phù hợp ngay lần đầu mở Vexere

Là khách lần đầu vào Vexere,
tôi muốn thấy sẵn ngôn ngữ, tiền tệ phù hợp,
để tôi không phải tìm cách đổi trước khi xem giá.

**Priority:** Should
**Screens:** SCR-12, SCR-13
**Common behaviors:** CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-26, BR-28, BR-29, BR-30, BR-31, BR-32, BR-33, BR-34, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Nếu khách mới (BR-29) mở Vexere lần đầu, giao diện hiển thị bằng ngôn ngữ tự nhận diện theo BR-29, khớp bảng quyết định cho khách mới (BR-30).
- AC2 (Happy) Done when: Nếu khách mới (BR-29) mở Vexere lần đầu, giá tham khảo hiển thị bằng tiền tệ tự nhận diện theo BR-25, khớp bảng quyết định cho khách mới (BR-30).
- AC3 (Happy) Done when: Nếu khách mới mở trên web một đường dẫn không có ngôn ngữ (BR-28), trang chuyển tới đường dẫn của ngôn ngữ tự nhận diện (BR-29).
- AC4 (Alternative) Done when: Nếu ngôn ngữ của trình duyệt hoặc thiết bị không khớp ngôn ngữ nào đang bật (BR-29), giao diện hiển thị bằng ngôn ngữ dự phòng của BR-29.
- AC5 (Error) Done when: Nếu không xác định được tín hiệu nào của khách mới (BR-29), Vexere mở bằng cặp ngôn ngữ và tiền tệ dự phòng của BR-29.
- AC6 (Happy) Done when: Nếu khách đã được tự nhận diện quay lại Vexere mà chưa chủ động chọn ngôn ngữ, tiền tệ nào (BR-26), kể cả khi truy cập từ quốc gia khác, Vexere dùng lại ngôn ngữ và tiền tệ đã tự nhận diện lần đầu (BR-31).
- AC7 (Alternative) Done when: Nếu trang được mở bởi bot của công cụ tìm kiếm (BR-29), trang hiển thị theo ngôn ngữ của đường dẫn, không bị tự nhận diện (BR-28).
- AC8 (Alternative) Done when: Nếu trang được mở bởi bot của công cụ tìm kiếm (BR-28), giá chỉ hiển thị VND.

**INVEST Check:** I / N / V / E / S / T

#### US-09 - Ngôn ngữ và tiền tệ chỉ định qua link

Là người chia sẻ link Vexere (marketing, affiliate),
tôi muốn link của tôi mở trang Vexere bằng ngôn ngữ, tiền tệ tôi chỉ định,
để người nhận thấy đúng thông tin tôi muốn.

**Priority:** Should
**Screens:** SCR-01, SCR-11, SCR-12, SCR-13
**Common behaviors:** CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-26, BR-29, BR-30, BR-31, BR-32, BR-33, BR-34, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Nếu người nhận mở link web có chỉ định ngôn ngữ và tiền tệ (BR-26), trang mở bằng đúng ngôn ngữ và tiền tệ đó.
- AC2 (Happy) Done when: Nếu người nhận mở deep link app có chỉ định ngôn ngữ và tiền tệ (BR-26), app mở bằng đúng ngôn ngữ và tiền tệ đó.
- AC3 (Alternative) Done when: Nếu người nhận là khách quay lại đã lưu lựa chọn chủ động khác với link (BR-26), phiên mở từ link vẫn dùng ngôn ngữ và tiền tệ của link.
- AC4 (Alternative) Done when: Nếu người nhận đổi ngôn ngữ hoặc tiền tệ trên picker trong phiên mở từ link (BR-26), Vexere dùng giá trị vừa đổi thay cho giá trị của link.
- AC5 (Alternative) Done when: Nếu người nhận đã có ngôn ngữ, tiền tệ đã lưu, phiên kế tiếp không mở từ link quay về các giá trị đã lưu đó (BR-31).
- AC6 (Alternative) Done when: Nếu người nhận đã đăng nhập, ngôn ngữ và tiền tệ trên hồ sơ không đổi theo giá trị của link (BR-31).
- AC7 (Error) Done when: Nếu tiền tệ chỉ định trên link nằm ngoài phạm vi tiền tệ của ngôn ngữ hiện hành (BR-34), giá tham khảo hiển thị bằng tiền tệ của ứng viên kế tiếp theo thứ tự ưu tiên (BR-26).
- AC8 (Error) Done when: Nếu ngôn ngữ chỉ định trên link chưa được bật (BR-22), trang mở bằng ngôn ngữ dự phòng của BR-22.

**INVEST Check:** I / N / V / E / S / T

### Epic 3 - Hiển thị kép

**Serves:** JTBD-01, JTBD-02

#### US-10 - Thấy giá tham khảo và VND ở mọi bước

Là khách inbound,
tôi muốn thấy đồng thời số tham khảo và số VND phải trả ở bất kỳ bước nào có giá,
để tôi luôn biết số thật sẽ bị trừ.

**Priority:** Must
**Screens:** SCR-01, SCR-02, SCR-03, SCR-04, SCR-05, SCR-07, SCR-08, SCR-09, SCR-10, SCR-11, SCR-20
**Common behaviors:** CB-01, CB-02, CB-03, CB-04, CB-05
**Rules applied (PRD Currency Switch):** BR-01, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-20, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-45, BR-47, BR-48, BR-49, BR-50, BR-51, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-62, BR-65, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Trên mọi bề mặt có giá dành cho khách thuộc phạm vi BR-05, mỗi giá được hiển thị kép, gồm số VND và số tham khảo bằng tiền tệ hiện hành (BR-05, BR-07).
- AC2 (Happy) Done when: Trong khi chế độ thứ bậc hiển thị là chế độ (1) "VND là số chính trên mọi bề mặt" (BR-06), mọi giá có số VND ở vị trí số chính và số tham khảo ở vị trí số phụ.
- AC3 (Alternative) Done when: Trong khi chế độ thứ bậc hiển thị là chế độ (2) "theo nhóm" (BR-06), mỗi bề mặt lấy số chính theo nhóm Browse hoặc Pay mà BR-06 gán cho bề mặt đó.
- AC4 (Alternative) Done when: Trong khi chế độ thứ bậc hiển thị là chế độ (2) "theo nhóm" (BR-06), số tiền của voucher và khuyến mãi vẫn lấy VND làm số chính trên mọi bề mặt (BR-20).
- AC5 (Happy) Done when: Số phụ có cỡ chữ nhỏ hơn và màu xám so với số chính (gợi ý cho Design: khoảng 70% cỡ chữ của số chính; DEP-04).
- AC6 (Alternative) Done when: Ở ô giá nhỏ (ví dụ lịch giá theo ngày, sơ đồ ghế), giá dùng biến thể gọn chỉ giảm cỡ chữ, vẫn hiển thị đủ số VND và số tham khảo (BR-07).
- AC7 (Happy) Done when: Trên mỗi trang có số tham khảo, MSG-01 hiện đúng một lần, cạnh bảng giá, không lặp ở từng giá; cách thể hiện theo thiết kế của từng UI (DEP-04).
- AC8 (Happy) Done when: Trên mọi trang có số tham khảo, khách mở được tooltip (i) cạnh MSG-01 và thấy MSG-02 với thông tin của bảng tỷ giá đang dùng cho các giá trên trang (BR-13, BR-51).
- AC9 (Happy) Done when: Từ tooltip MSG-02, khách mở được mục tỷ giá tham khảo của Điều khoản (SCR-20), nơi hiển thị MSG-15.
- AC10 (Happy) Done when: Nếu khách đổi tiền tệ ở trang kết quả tìm kiếm, toàn bộ giá trên trang được hiển thị kép theo tiền tệ mới trong thời gian NFR-01, khách không phải tìm lại chuyến.
- AC11 (Happy) Done when: Cùng một giá (ví dụ cùng một dòng breakdown của cùng một đơn) hiển thị cùng một số tham khảo trên mọi platform và mọi nơi hiển thị (NFR-03, NFR-04).
- AC12 (Alternative) Done when: Trong khi màn thanh toán còn chờ kết luận của Legal (BR-65), màn thanh toán (SCR-07) chỉ hiển thị VND, không có số tham khảo.

**INVEST Check:** I / N / V / E / S / T
- I: chưa đạt, cần bảng tỷ giá (US-19) và quy ước định dạng số (US-01) có trước.
- S: chưa đạt, phủ 10 bề mặt có giá trên 3 platform; nên tách theo nhóm bề mặt (xem và chọn chuyến; checkout và thanh toán; sau khi đặt) khi lập sprint.

#### US-11 - Breakdown cộng đúng bằng total

Là khách inbound,
tôi muốn các dòng breakdown cộng lại đúng bằng total quy đổi,
để tôi tin giá không bị cộng sai.

**Priority:** Must
**Screens:** SCR-05, SCR-07, SCR-08, SCR-09
**Common behaviors:** CB-01, CB-02, CB-03, CB-04, CB-05
**Rules applied (PRD Currency Switch):** BR-01, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-45, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-62, BR-65, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Trên mọi bề mặt hiển thị breakdown (SCR-05, SCR-07, SCR-08, SCR-09), số tham khảo của các dòng breakdown cộng khớp số tham khảo của total (BR-17, BR-18).
- AC2 (Happy) Done when: Số tham khảo của total hiển thị đúng kết quả quy đổi theo BR-15.
- AC3 (Happy) Done when: Số tham khảo của dòng voucher theo %, dòng có mức trần và dòng phí được quy đổi từ số VND đã tính của chính dòng đó (BR-16).
- AC4 (Alternative) Done when: Nếu đơn có dòng giảm giá, số tham khảo của từng dòng breakdown hiển thị đúng như tính theo BR-17, kể cả khi đơn có nhiều dòng giảm giá.
- AC5 (Alternative) Done when: Nếu đơn không có dòng giảm giá, số tham khảo của từng dòng breakdown hiển thị đúng như tính theo BR-18.
- AC6 (Alternative) Done when: Nếu đơn có nhiều vé, dòng vé trên breakdown hiển thị số tham khảo tính theo quy tắc đơn nhiều vé (BR-19), có thể khác tổng các số tham khảo theo đơn giá trên sơ đồ ghế.
- AC7 (Happy) Done when: Email xác nhận (SCR-08) và My bookings (SCR-09) hiển thị breakdown và total với số tham khảo đã lưu trên đơn (BR-42, BR-44).

**INVEST Check:** I / N / V / E / S / T
- I: chưa đạt, cần bảng tỷ giá (US-19) và hiển thị kép (US-10) có trước.

#### US-12 - Lọc chuyến theo tiền tham khảo

Là khách inbound,
tôi muốn lọc chuyến theo khoảng giá bằng tiền tệ đã chọn,
để tôi tìm chuyến trong ngân sách.

**Priority:** Should
**Screens:** SCR-01
**Common behaviors:** CB-01, CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-21, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Trên trang kết quả tìm kiếm (SCR-01), khách chọn được giá trị biên của khoảng giá trên bộ lọc và thanh trượt giá bằng tiền tệ tham khảo hiện hành.
- AC2 (Happy) Done when: Giá trị biên trên bộ lọc và thanh trượt giá hiển thị dạng xấp xỉ, có tiền tố "~", với mã tiền tệ và số lẻ theo BR-09, BR-11, BR-12.
- AC3 (Happy) Done when: Sau khi khách áp dụng khoảng giá, danh sách chuyến chỉ còn các chuyến được giữ theo quy tắc lọc giá theo tiền tham khảo (BR-21).
- AC4 (Alternative) Done when: Chuyến có số tham khảo hiển thị đúng bằng giá trị biên khách đã chọn vẫn có trong kết quả lọc (BR-21).
- AC5 (Alternative) Done when: Nếu không chuyến nào được giữ theo khoảng giá đã chọn (BR-21), trang kết quả hiển thị trạng thái không có chuyến hiện có của trang kết quả tìm kiếm.

**INVEST Check:** I / N / V / E / S / T
- I: chưa đạt, cần bảng tỷ giá (US-19) và hiển thị kép (US-10) có trước.
- E: chưa đạt hoàn toàn, chờ Q-20 (giá trị biên có kèm số VND hay không) và Q-21 (đổi tiền tệ khi đang lọc).

### Epic 4 - Checkout

**Serves:** JTBD-02

#### US-13 - Thông báo thanh toán rõ ràng

Là khách inbound ở checkout,
tôi muốn thấy rõ số VND chính xác sẽ bị trừ cùng lưu ý về tỷ giá của ngân hàng,
để tôi không bất ngờ khi xem sao kê.

**Priority:** Must
**Screens:** SCR-05, SCR-07, SCR-12, SCR-13
**Common behaviors:** CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-02, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-39, BR-40, BR-41, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-65, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Ở checkout, dòng MSG-07 hiện ngay dưới tổng tiền.
- AC2 (Happy) Done when: Ở checkout, hộp Payment Notice bản đầy đủ hiện MSG-08, với số VND của báo giá (BR-39) và số tham khảo giống hệt tổng tham khảo ở dòng total (BR-15, NFR-03).
- AC3 (Happy) Done when: Ở màn thanh toán, Payment Notice rút gọn hiện MSG-09 thành một dòng ngay trên nút thanh toán, với số VND của báo giá (BR-39).
- AC4 (Happy) Done when: Ở màn thanh toán, nhãn nút thanh toán là MSG-10 bằng ngôn ngữ UI, với số VND của báo giá (BR-39) viết theo BR-12.
- AC5 (Happy) Done when: Ở màn thanh toán, MSG-11 hiện thành một dòng ngay dưới nút thanh toán.
- AC6 (Happy) Done when: Ở màn thanh toán, khách bấm nút thanh toán là thanh toán được, không có ô tick đồng ý nào phải chọn trước.
- AC7 (Alternative) Done when: Ở màn thanh toán, picker ngôn ngữ và picker tiền tệ chỉ đọc: khách thấy ngôn ngữ và tiền tệ hiện hành nhưng không đổi được (BR-40).
- AC8 (Alternative) Done when: Nếu khách đổi tiền tệ trước màn thanh toán (BR-40), hộp Payment Notice ở checkout hiện số tham khảo bằng tiền tệ mới trong khi số VND giữ nguyên (BR-39).
- AC9 (Alternative) Done when: Nếu bản dịch Payment Notice của ngôn ngữ UI chưa được duyệt (BR-41), MSG-08 và MSG-09 hiện bằng bản EN.
- AC10 (Alternative) Done when: Trong khi checkout hoặc màn thanh toán chỉ hiển thị VND (CB-02, CB-03, CB-04), hoặc màn thanh toán đang chờ kết luận của Legal (BR-65), màn đó không hiện MSG-08 hay MSG-09 (assumed, A-20).

**INVEST Check:** I / N / V / E / S / T

#### US-14 - Tỷ giá tham khảo được làm mới khi quá hạn

Là khách inbound đang thanh toán,
tôi muốn số tham khảo được cập nhật theo tỷ giá mới mà không bị chặn thanh toán,
để tôi tiếp tục đặt vé mà không mất thời gian điền lại thông tin.

**Priority:** Must
**Screens:** SCR-05, SCR-06, SCR-07, SCR-01
**Common behaviors:** CB-02, CB-03, CB-04
**Rules applied (PRD Currency Switch):** BR-01, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-39, BR-42, BR-43, BR-44, BR-46, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-66, BR-67, BR-68, BR-69, BR-70, BR-71, BR-72, BR-74, BR-75, BR-76, BR-77, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Trong khi tỷ giá của báo giá còn hiệu lực (BR-66), số tham khảo của cùng một tiền tệ ở checkout, bước nhập thông tin hành khách và màn thanh toán không đổi, kể cả khi đã có bảng tỷ giá hiện hành mới hơn (BR-39, BR-48).
- AC2 (Happy) Done when: Nếu tới mốc hết hiệu lực tỷ giá của báo giá và báo giá chuyển sang bảng tỷ giá mới (BR-67), số tham khảo ở checkout, bước nhập thông tin hành khách và màn thanh toán hiển thị theo bảng tỷ giá mới của báo giá.
- AC3 (Happy) Done when: Sau khi báo giá chuyển sang bảng tỷ giá mới (BR-67), số VND và mốc hết giữ chỗ không đổi (BR-39).
- AC4 (Happy) Done when: Sau khi báo giá chuyển sang bảng tỷ giá mới (BR-67), khách vẫn ở bước đang làm và không phải nhập lại thông tin hành khách đã nhập.
- AC5 (Happy) Done when: Nếu tổng tham khảo khách đang thấy thay đổi khi báo giá chuyển sang bảng tỷ giá mới (BR-67), toast hiện MSG-12.
- AC6 (Happy) Done when: Trong khi chỗ vẫn còn được giữ, việc tới mốc hết hiệu lực tỷ giá của báo giá không chặn thanh toán, dù báo giá đã chuyển sang bảng tỷ giá mới (BR-67) hay giữ tỷ giá hiện có (BR-68): khách bấm nút thanh toán và thanh toán được mà không phải xác nhận lại giá.
- AC7 (Happy) Done when: Nếu khách thanh toán thành công sau khi báo giá đã chuyển sang bảng tỷ giá mới (BR-67), số tham khảo lưu trên đơn khi báo giá thành đơn (BR-70) giống hệt tổng tham khảo khách thấy ở màn thanh toán (NFR-03).
- AC8 (Alternative) Done when: Nếu tổng tham khảo không đổi khi tới mốc hết hiệu lực tỷ giá của báo giá, dù báo giá đã chuyển sang bảng tỷ giá mới (BR-67) hay giữ tỷ giá hiện có (BR-68), không có toast MSG-12.
- AC9 (Error) Done when: Nếu tới mốc hết hiệu lực tỷ giá của báo giá mà chưa lấy được bảng tỷ giá hợp lệ mới (BR-68), số tham khảo vẫn hiển thị theo tỷ giá hiện có của báo giá.
- AC10 (Error) Done when: Nếu hết thời gian giữ chỗ (BR-69) khi khách đang ở checkout, bước nhập thông tin hành khách hoặc màn thanh toán, khách được đưa về trang kết quả tìm kiếm (SCR-01) để chọn lại chuyến (BR-74), và trang hiện MSG-13.

**INVEST Check:** I / N / V / E / S / T

### Epic 5 - Sau khi đặt

**Serves:** JTBD-02, JTBD-06, JTBD-07

#### US-15 - Đơn đã đặt giữ số tham khảo lúc đặt

Là khách đã đặt vé,
tôi muốn email xác nhận, My bookings hiện số tham khảo theo tỷ giá lúc đặt,
để số tôi thấy khớp với lúc thanh toán.

**Priority:** Must
**Screens:** SCR-08, SCR-09
**Common behaviors:** CB-03, CB-05
**Rules applied (PRD Currency Switch):** BR-01, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-45, BR-46, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-62, BR-65, BR-66, BR-68, BR-70, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Nếu khách thanh toán thành công, báo giá chuyển sang trạng thái Đã thành đơn (BR-70).
- AC2 (Happy) Done when: My bookings hiển thị đơn với số VND kèm số tham khảo bằng tiền tệ tham khảo lưu trên đơn (BR-44).
- AC3 (Happy) Done when: Email xác nhận của đơn hiển thị số VND kèm số tham khảo bằng tiền tệ tham khảo lưu trên đơn (BR-44).
- AC4 (Happy) Done when: Số tham khảo của đơn trên email xác nhận và My bookings giống hệt số tham khảo khách đã thấy ở màn thanh toán của đơn đó (BR-42, NFR-03).
- AC5 (Alternative) Done when: Nếu bảng tỷ giá hiện hành đã đổi sau khi đặt (BR-48), My bookings vẫn hiển thị số tham khảo lúc đặt của đơn, không tính lại theo bảng mới (BR-44).
- AC6 (Alternative) Done when: Nếu sau khi đặt khách đổi tiền tệ, hoặc đổi sang một ngôn ngữ khác VI (BR-44), đơn cũ trên My bookings vẫn hiển thị tiền tệ tham khảo và số tham khảo lúc đặt.
- AC7 (Alternative) Done when: Trong khi khách xem My bookings trên UI VI (BR-44), đơn chỉ hiển thị số VND.
- AC8 (Error) Done when: Nếu số tham khảo hiển thị trên thiết bị của khách lúc thanh toán bị sai lệch (BR-42), email xác nhận và My bookings hiển thị số tham khảo do Vexere tính lại, không phải số trên thiết bị.
- AC9 (Happy) Done when: Email xác nhận và vé điện tử của đơn được gửi bằng ngôn ngữ đặt vé (BR-46).
- AC10 (Alternative) Done when: Nếu ngôn ngữ đặt vé là VI (BR-46), email xác nhận và vé điện tử chỉ có số VND.
- AC11 (Alternative) Done when: Nếu khách đổi ngôn ngữ trên app sau khi thanh toán (BR-46), thông báo trên app về đơn dùng ngôn ngữ mới.

**INVEST Check:** I / N / V / E / S / T (S: gồm cả ngôn ngữ của email, vé điện tử và thông báo app (BR-46); nếu vượt một sprint, tách AC9 đến AC11 thành story riêng)

#### US-16 - Hoàn tiền theo tỷ giá ngày mua

Là khách được hoàn tiền,
tôi muốn thấy số hoàn bằng VND kèm số tham khảo theo tỷ giá ngày mua,
để tôi nắm được số tiền được hoàn.

**Priority:** Must
**Screens:** SCR-10
**Common behaviors:** CB-03, CB-05
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-45, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-62, BR-65, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Thông tin hoàn tiền của đơn hiển thị số hoàn bằng VND làm số chính, kèm số tham khảo bằng tiền tệ tham khảo của đơn (BR-45).
- AC2 (Happy) Done when: Nếu tỷ giá hiện hành ngày hoàn đã khác tỷ giá lúc mua (BR-48), số tham khảo của số hoàn vẫn được quy đổi theo bảng tỷ giá lưu trên đơn (BR-45).
- AC3 (Happy) Done when: Trong khi số hoàn hiển thị kèm số tham khảo (BR-45), MSG-14 hiển thị ngay cạnh số hoàn.
- AC4 (Happy) Done when: Số hoàn và số tham khảo của số hoàn hiển thị cho khách mà không có bước nào yêu cầu khách đồng ý (BR-45).
- AC5 (Happy) Done when: Số tham khảo của số hoàn giống hệt nhau mỗi lần khách xem lại và trên mọi platform (BR-45, NFR-03).
- AC6 (Alternative) Done when: Nếu sau khi đặt khách đổi tiền tệ, hoặc đổi sang một ngôn ngữ khác VI (BR-45), số tham khảo của số hoàn vẫn dùng tiền tệ tham khảo của đơn.
- AC7 (Alternative) Done when: Trong khi khách xem thông tin hoàn tiền trên UI VI (BR-08), số hoàn chỉ hiển thị VND.

**INVEST Check:** I / N / V / E / S / T (I: cần bảng tỷ giá và tiền tệ tham khảo lưu trên đơn khi thanh toán (BR-70, US-15-AC1); làm cùng hoặc sau US-15)

#### US-17 - Thông tin tiền tệ của đơn cho CSKH

Là nhân viên CSKH,
tôi muốn xem tiền tệ, số tham khảo, tỷ giá, thông báo khách đã thấy trên từng đơn,
để tôi xử lý ticket "giá khác số bị trừ" bằng bằng chứng.

**Priority:** Must
**Screens:** SCR-15
**Common behaviors:** CB-05
**Rules applied (PRD Currency Switch):** BR-01, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-45, BR-46, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-62, BR-65, BR-66, BR-68, BR-70, BR-71, BR-75, BR-76, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Back office đơn hàng hiển thị tiền tệ tham khảo và số tham khảo của đơn (BR-70).
- AC2 (Happy) Done when: Back office đơn hàng hiển thị tỷ giá và nguồn tỷ giá đã dùng để tính số tham khảo của đơn (BR-70).
- AC3 (Happy) Done when: Back office đơn hàng hiển thị nhóm hiển thị Browse/Pay đã áp dụng cho đơn (BR-06, BR-70).
- AC4 (Happy) Done when: Back office đơn hàng hiển thị phiên bản, ngôn ngữ và thời điểm MSG-01 được hiển thị cho khách (BR-70).
- AC5 (Happy) Done when: Số tiền của đơn trên back office hiển thị kép (BR-05), số chính theo chế độ thứ bậc hiển thị (BR-06).
- AC6 (Happy) Done when: Số tham khảo của đơn trên back office giống hệt số trên email xác nhận và My bookings của cùng đơn (NFR-03).

**INVEST Check:** I / N / V / E / S / T (I: cần thông tin tiền tệ lưu trên đơn khi thanh toán (BR-70, US-15-AC1); làm cùng hoặc sau US-15)

#### US-18 - Hoá đơn và báo cáo doanh thu theo VND

Là kế toán của Vexere (gồm Finance analyst),
tôi muốn nhận hoá đơn, mọi số liệu doanh thu bằng VND,
để báo cáo không bị lẫn số tham khảo.

**Priority:** Must
**Screens:** none
**Common behaviors:** none
**Rules applied (PRD Currency Switch):** BR-01, BR-02, BR-03, BR-04, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-45, BR-46, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-66, BR-68, BR-70, BR-71, BR-75, BR-76, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Hoá đơn VAT của một đơn có số tham khảo được xuất bằng VND theo BR-03.
- AC2 (Happy) Done when: Hoá đơn VAT của đơn không có dòng phí quy đổi ngoại tệ (BR-02).
- AC3 (Happy) Done when: Đối soát thanh toán của một đơn có số tham khảo dùng số tiền VND khách đã thanh toán (BR-01).
- AC4 (Happy) Done when: Báo cáo doanh thu ghi nhận đơn có số tham khảo bằng số tiền VND của đơn (BR-04).
- AC5 (Alternative) Done when: Nếu đơn có số tham khảo (BR-70), tiền tệ tham khảo và số tham khảo chỉ đi kèm là thông tin phụ trong số liệu doanh thu, không được cộng vào chỉ tiêu doanh thu nào (BR-04).
- AC6 (Alternative) Done when: Nếu hai đơn có cùng số tiền VND nhưng khác tiền tệ tham khảo, hoặc một trong hai đơn không có số tham khảo (BR-43), hai đơn có cùng số liệu trên hoá đơn VAT, đối soát và báo cáo doanh thu (BR-01, BR-03, BR-04).
- AC7 (Alternative) Done when: Nếu đơn được hoàn tiền (BR-45), số hoàn được ghi nhận trong đối soát và báo cáo doanh thu bằng số VND của số hoàn (BR-01, BR-04).

**INVEST Check:** I / N / V / E / S / T

### Epic 6 - Vận hành

**Serves:** JTBD-08, JTBD-09

#### US-19 - Bảng tỷ giá thống nhất

Là nhân viên vận hành tỷ giá,
tôi muốn có một bảng tỷ giá thống nhất được cập nhật định kỳ từ các nguồn đã cấu hình,
để số tham khảo khách thấy luôn dựa trên tỷ giá đúng và nhất quán trong một phiên.

**Priority:** Must
**Screens:** SCR-16
**Common behaviors:** CB-02
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-66, BR-68, BR-71, BR-72, BR-73, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Sau mỗi lần cập nhật định kỳ tạo được bảng tỷ giá hợp lệ (BR-48, BR-49), bảng đó thành bảng tỷ giá hiện hành: trên SCR-16, tỷ giá hiện tại của mọi cặp có quy tắc đang bật đổi sang tỷ giá, nguồn và thời điểm bản tin của bảng mới.
- AC2 (Happy) Done when: Trong bảng tỷ giá mới, mỗi cặp lấy tỷ giá từ nguồn có ưu tiên cao nhất đang bật trong quy tắc của cặp (BR-47, BR-52), và SCR-16 hiện nguồn đó ở tỷ giá hiện tại của cặp.
- AC3 (Alternative) Done when: Nếu nguồn ưu tiên cao nhất của một cặp lỗi hoặc không có cặp đó (BR-47), cặp đó trong bảng mới lấy tỷ giá từ nguồn kế tiếp đang bật, và SCR-16 hiện nguồn kế tiếp đó.
- AC4 (Happy) Done when: Trong một phiên, cùng một số VND hiển thị cùng một số tham khảo trên mọi trang có giá (BR-48); trường hợp phiên kéo dài qua một lần cập nhật chờ Q-16.
- AC5 (Alternative) Done when: Nếu tỷ giá mới của một cặp lệch quá biến động tối đa/ngày của quy tắc (BR-54) và cài đặt thử nguồn kế tiếp của cặp là Không (BR-55), bảng mới giữ tỷ giá hiện hành của cặp: SCR-16 vẫn hiện tỷ giá, nguồn và thời điểm bản tin cũ của cặp.
- AC6 (Alternative) Done when: Nếu tỷ giá mới của một cặp bị bỏ qua theo BR-54 và cài đặt thử nguồn kế tiếp của cặp là Có (BR-55), tỷ giá của cặp trong bảng mới được xác định từ nguồn kế tiếp theo BR-55, và SCR-16 hiện nguồn được dùng.
- AC7 (Alternative) Done when: Nếu tỷ giá mới của một cặp bị bỏ qua theo BR-54, một cảnh báo về tỷ giá bị bỏ qua của cặp đó được ghi lại.
- AC8 (Error) Done when: Nếu một lần cập nhật không tạo được bảng tỷ giá hợp lệ (BR-49), kể cả khi mọi nguồn đều lỗi, bảng tỷ giá hiện hành giữ nguyên (BR-56): số tham khảo khách thấy và tỷ giá hiện tại trên SCR-16 không đổi.
- AC9 (Error) Done when: Nếu số lần cập nhật liên tiếp không tạo được bảng tỷ giá hợp lệ đạt ngưỡng bảng cũ (BR-56), bảng tỷ giá hiện hành chuyển sang Cũ (BR-71).
- AC10 (Alternative) Done when: Nếu nguồn không công bố bản tin trong ngày (BR-56), các lần cập nhật không có bản tin mới trong ngày đó không được tính vào ngưỡng bảng cũ, và bảng tỷ giá hiện hành không chuyển sang Cũ vì những lần này.
- AC11 (Alternative) Done when: Nếu bảng tỷ giá hiện hành đang Cũ và một lần cập nhật tạo được bảng hợp lệ trong khi công tắc tắt khẩn cấp không bật (BR-73), bảng mới thành bảng tỷ giá hiện hành và các bề mặt có giá hiện lại số tham khảo.
- AC12 (Happy) Done when: Mỗi lần cập nhật, tỷ giá mới của từng cặp được ghi vào lịch sử thay đổi tỷ giá theo BR-57, và lịch sử này tra lại được trong thời gian NFR-02.

**INVEST Check:** I / N / V / E / S / T
- I (chưa đạt): cần quy tắc tỷ giá đang bật và danh sách SCR-16 của US-22 (hoặc quy tắc mẫu) để chạy và kiểm thử.
- E (chưa đạt): AC4 cần PO cùng Dev / Tech Lead chốt Q-16 trước khi ước lượng.
- S (chưa đạt): nhiều nhánh; nếu vượt một sprint, tách biến động tối đa/ngày (AC5 đến AC7) và bảng cũ (AC8 đến AC11) thành story riêng.

#### US-20 - Thêm ngôn ngữ hoặc tiền tệ bằng cấu hình

Là PO,
tôi muốn bật thêm ngôn ngữ, tiền tệ mới bằng cấu hình,
để tôi mở thị trường mới mà không phụ thuộc lịch phát hành.

**Priority:** Should
**Screens:** SCR-12, SCR-13, SCR-17, SCR-18, SCR-19
**Common behaviors:** none
**Rules applied (PRD Currency Switch):** BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-26, BR-29, BR-30, BR-31, BR-32, BR-33, BR-34, BR-35, BR-36, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-64, BR-66, BR-68, BR-71, BR-75, BR-76, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Trên SCR-18, bản dịch cho một ngôn ngữ mới được tạo từ bản EN (en-US), cho cả web và app (luồng đề xuất, chờ Q-08).
- AC2 (Happy) Done when: Trên SCR-19, PO xem trước được UI web và app với bản dịch mới trước khi bật ngôn ngữ đó (luồng đề xuất, chờ Q-08).
- AC3 (Alternative) Done when: Trong khi bản dịch của ngôn ngữ mới đã được đưa lên hệ thống nhưng ngôn ngữ chưa được bật (BR-22, BR-35), khách không thấy ngôn ngữ đó trên picker ngôn ngữ (SCR-12).
- AC4 (Happy) Done when: Sau khi một ngôn ngữ đã có bản dịch trên hệ thống được bật (BR-22, BR-35), ngôn ngữ đó xuất hiện trên picker ngôn ngữ (SCR-12) ở mọi platform (NFR-04) mà không cần phát hành bản mới.
- AC5 (Error) Done when: Nếu bản dịch của một ngôn ngữ chưa được đưa lên hệ thống (BR-35), ngôn ngữ đó không bật được và vẫn không xuất hiện trên picker ngôn ngữ.
- AC6 (Happy) Done when: Sau khi một tiền tệ mới được bật và thêm vào phạm vi tiền tệ của một ngôn ngữ (BR-22, BR-23), và bảng tỷ giá hiện hành đã có cặp của tiền tệ đó, tiền tệ đó xuất hiện trên picker tiền tệ (SCR-13) của ngôn ngữ đó mà không cần phát hành bản mới.
- AC7 (Error) Done when: Nếu một tiền tệ đã được bật nhưng bảng tỷ giá hiện hành chưa có cặp của nó (BR-23, BR-52), tiền tệ đó chưa xuất hiện trên picker tiền tệ.
- AC8 (Happy) Done when: Mỗi thay đổi cấu hình ngôn ngữ, tiền tệ, phạm vi tiền tệ của ngôn ngữ và bảng quốc gia → tiền tệ được ghi vào lịch sử thay đổi cấu hình theo BR-36.
- AC9 (Alternative) Done when: Nếu một ngôn ngữ hoặc tiền tệ mà khách đã lưu bị tắt (BR-64, đề xuất, A-12), khách thấy ngôn ngữ, tiền tệ được xác định lại theo BR-64 thay cho lựa chọn đã lưu.
- AC10 (Alternative) Done when: Nếu ngôn ngữ hoặc tiền tệ đó được bật lại (BR-64), khách thấy lại lựa chọn đã lưu mà không phải chọn lại.
- AC11 (Error) Done when: Nếu người thực hiện không có quyền theo BR-76, việc bật, tắt ngôn ngữ, tiền tệ hoặc sửa phạm vi tiền tệ, bảng quốc gia → tiền tệ không được thực hiện theo phân quyền hiện có (DEP-15), và cấu hình đang có giữ nguyên.

**INVEST Check:** I / N / V / E / S / T
- I (chưa đạt): AC6, AC7 cần quy tắc tỷ giá (US-22) và bảng tỷ giá (US-19); AC3, AC4, AC6 kiểm tra trên picker của US-05, US-06.
- E (chưa đạt): luồng tạo, xem trước bản dịch và SCR-18, SCR-19 chờ Dev / Tech Lead xác nhận (Q-08).
- S (chưa đạt): story gộp thêm ngôn ngữ (AC1 đến AC5) và thêm tiền tệ (AC6, AC7); nên tách làm hai story.

#### US-21 - Bật tắt và ramp tính năng

Là PO,
tôi muốn bật tắt Currency Switch theo từng vertical × platform,
để tôi ramp an toàn và tắt ngay khi có sự cố.

**Priority:** Must
**Screens:** none
**Common behaviors:** CB-02, CB-03, CB-05
**Rules applied (PRD Currency Switch):** BR-01, BR-05, BR-06, BR-07, BR-08, BR-09, BR-10, BR-11, BR-12, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-45, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-61, BR-62, BR-63, BR-65, BR-66, BR-68, BR-71, BR-72, BR-73, BR-75, BR-76, BR-77, BR-78, BR-79

**Acceptance Criteria**

- AC1 (Happy) Done when: Sau khi PO bật Currency Switch cho một vertical × platform (BR-60), khách dùng UI ngoại ngữ với tiền tệ tham khảo khác VND trên vertical × platform đó thấy giá hiển thị kép (BR-05) mà không cần phát hành bản mới.
- AC2 (Happy) Done when: Bật hoặc tắt Currency Switch cho một vertical × platform không làm đổi trạng thái của các vertical × platform khác (BR-60).
- AC3 (Happy) Done when: Trong khi Currency Switch bật cho một vertical × platform ở một tỷ lệ traffic (BR-60), chỉ phần khách thuộc tỷ lệ đó thấy số tham khảo; khách còn lại thấy như CB-03.
- AC4 (Happy) Done when: Sau khi PO đổi tỷ lệ traffic của một vertical × platform (BR-60), tỷ lệ mới có hiệu lực mà không cần phát hành bản mới.
- AC5 (Happy) Done when: Sau khi PO tắt Currency Switch cho một vertical × platform (BR-61, đề xuất, A-12), mọi bề mặt của vertical × platform đó chuyển sang như CB-03 mà không cần phát hành bản mới.
- AC6 (Alternative) Done when: Nếu Currency Switch được bật lại cho vertical × platform đó (BR-61), đơn đã lưu số tham khảo trước khi tắt hiện lại số tham khảo lúc đặt trên My bookings (BR-44).
- AC7 (Alternative) Done when: Nếu khách đã vào checkout trước khi Currency Switch được bật cho vertical × platform đó (BR-63, đề xuất, A-12), checkout đó giữ cách hiển thị như trước khi bật cho tới khi xong đơn.
- AC8 (Happy) Done when: Sau khi người có quyền theo BR-77 bật công tắc tắt khẩn cấp, bảng tỷ giá hiện hành chuyển sang Cũ (BR-72) mà không cần phát hành bản mới.
- AC9 (Alternative) Done when: Nếu công tắc tắt khẩn cấp được tắt, bảng tỷ giá hiện hành trở lại Hợp lệ ở lần cập nhật kế tiếp tạo được bảng hợp lệ (BR-73).
- AC10 (Error) Done when: Nếu người thực hiện không có quyền theo BR-77, việc bật tắt Currency Switch, đổi tỷ lệ traffic hoặc bật tắt công tắc tắt khẩn cấp không được thực hiện theo phân quyền hiện có (DEP-15), và trạng thái đang có giữ nguyên.

**INVEST Check:** I / N / V / E / S / T
- E (chưa đạt): cách vận hành bật tắt, ramp và công tắc tắt khẩn cấp chờ Q-10; picker và thông báo trong lúc tắt chờ Q-15.

#### US-22 - Cấu hình tỷ giá trên công cụ

Là nhân viên vận hành tỷ giá,
tôi muốn quản lý quy tắc tỷ giá quy đổi sang VND trên công cụ cấu hình nội bộ VEX-CONFIG,
để tôi thêm cặp tiền, đổi nguồn tỷ giá hoặc tắt một cặp mà không cần Dev.

**Priority:** Must
**Screens:** SCR-16, SCR-17
**Common behaviors:** CB-02
**Rules applied (PRD Currency Switch):** BR-01, BR-08, BR-09, BR-10, BR-11, BR-13, BR-14, BR-15, BR-16, BR-17, BR-18, BR-19, BR-22, BR-23, BR-25, BR-42, BR-43, BR-44, BR-47, BR-48, BR-49, BR-52, BR-53, BR-54, BR-55, BR-56, BR-57, BR-58, BR-59, BR-60, BR-66, BR-68, BR-71, BR-72, BR-75, BR-76, BR-77, BR-78

**Acceptance Criteria**

- AC1 (Happy) Done when: Danh sách quy tắc trên SCR-16 hiện mỗi quy tắc với: ID, cặp tiền, buffer, các nguồn theo thứ tự ưu tiên, tỷ giá hiện tại theo quy tắc kèm tỷ giá gốc, nguồn và thời điểm cập nhật, người và thời điểm sửa gần nhất, trạng thái (BR-48, BR-52).
- AC2 (Happy) Done when: Trên SCR-16, lọc theo mã tiền hoặc theo trạng thái (Tất cả, Đang bật, Đang tắt) chỉ hiện các quy tắc khớp bộ lọc.
- AC3 (Happy) Done when: Từ nút thêm cấu hình tỷ giá trên SCR-16, nhân viên vận hành tỷ giá nhập quy tắc đúng BR-58 cho một cặp tiền chưa có quy tắc trên SCR-17, và sau khi lưu, quy tắc mới xuất hiện trong danh sách SCR-16 (BR-52).
- AC4 (Error) Done when: Nếu dữ liệu nhập trên SCR-17 không đúng BR-58, quy tắc không được lưu và lỗi inline dưới từng trường sai hiện MSG-21.
- AC5 (Error) Done when: Nếu tạo quy tắc cho một cặp tiền đã có quy tắc (BR-59), quy tắc không được tạo và form hiện MSG-20.
- AC6 (Alternative) Done when: Bấm link trong MSG-20 mở quy tắc đang có của cặp đó trên SCR-17.
- AC7 (Happy) Done when: Trên form sửa quy tắc (SCR-17), các trường mà BR-58 không cho sửa sau khi tạo hiển thị ở dạng chỉ đọc; các trường còn lại sửa và lưu được.
- AC8 (Happy) Done when: Sau khi lưu một quy tắc vừa tạo hoặc vừa sửa, một lần cập nhật tỷ giá được thực hiện theo BR-48; khi lần đó tạo được bảng hợp lệ (BR-49), SCR-16 hiện tỷ giá hiện tại của cặp với thời điểm cập nhật mới.
- AC9 (Happy) Done when: Bấm làm mới tỷ giá trên SCR-16 thực hiện một lần cập nhật tỷ giá (BR-48); khi lần đó tạo được bảng hợp lệ (BR-49), danh sách hiện tỷ giá hiện tại theo bảng mới.
- AC10 (Happy) Done when: Sau khi đổi số ưu tiên hoặc bật, tắt một nguồn của một cặp trên SCR-17 (BR-47, BR-58), SCR-16 hiện cặp đó lấy tỷ giá từ nguồn có ưu tiên cao nhất đang bật theo cấu hình mới.
- AC11 (Happy) Done when: Trên SCR-17, nhân viên vận hành tỷ giá chọn được cho một cặp việc buffer có áp vào số tham khảo hay không (BR-14); sau khi lưu, số tham khảo của tiền tệ đó quy đổi theo lựa chọn mới từ bảng tỷ giá tạo sau đó (BR-13).
- AC12 (Happy) Done when: Trên SCR-17, nhân viên vận hành tỷ giá chọn được cho một cặp việc có thử nguồn kế tiếp khi tỷ giá mới bị bỏ qua hay không (BR-55); lựa chọn đã lưu hiện lại khi mở lại quy tắc và được dùng ở các lần cập nhật sau.
- AC13 (Happy) Done when: Nhân viên vận hành tỷ giá đặt được ngưỡng bảng cũ (BR-56) mà không cần Dev; các lần cập nhật sau đó xét bảng cũ theo ngưỡng đã lưu (BR-71).
- AC14 (Alternative) Done when: Nếu nhân viên vận hành tỷ giá tắt quy tắc của một cặp (BR-53), tiền tệ đó không còn trên picker tiền tệ (SCR-13) kể từ khi cặp đó ra khỏi bảng tỷ giá hiện hành (BR-23).
- AC15 (Alternative) Done when: Nếu một quy tắc đang tắt được bật lại, tiền tệ đó xuất hiện lại trên picker tiền tệ khi bảng tỷ giá hiện hành có lại cặp đó (BR-23, BR-48).
- AC16 (Happy) Done when: Mỗi lần tạo, sửa, bật, tắt một quy tắc hoặc một nguồn được ghi vào lịch sử thay đổi quy tắc tỷ giá theo BR-57, và lịch sử này tra lại được trong thời gian NFR-02.
- AC17 (Error) Done when: Nếu người thực hiện không có quyền theo BR-78, việc tạo, sửa, bật tắt quy tắc hoặc nguồn, đặt ngưỡng bảng cũ hay làm mới tỷ giá không được thực hiện theo phân quyền hiện có (DEP-15), và cấu hình đang có giữ nguyên.

**INVEST Check:** I / N / V / E / S / T
- E (chưa đạt): tắt quy tắc của tiền tệ chính của một ngôn ngữ đang bật chờ Q-14; tiền tệ bị tắt chuyển sang ứng viên kế tiếp hay chỉ VND chờ Q-17; cách làm mới tỷ giá ngay sau khi tạo, sửa chờ Q-09.
- S (chưa đạt): 17 AC; nên tách thành danh sách, lọc và làm mới (AC1, AC2, AC9), tạo và sửa quy tắc (AC3 đến AC8, AC10), cài đặt và bật tắt (AC11 đến AC15).

## 8. Assumptions & Open Questions

**Assumptions**

| ID | Assumption | Affects | Source / Confidence |
|----|------------|---------|---------------------|
| A-01 | Nguồn của brief là PRD - Currency Switch (Multi-currency Display & Settlement) v0.1, 09 Oct 2026, PO Nguyễn Đức Anh Tuấn. BRD Currency Switch chưa được cung cấp. | DEP-13 | Brief (Assumptions) / Cao |
| A-02 | Problem Statement và JTBD được suy ra từ Goals và vế "để..." của các US, vì PRD gốc không có hai mục này. | JTBD-01 đến JTBD-09 | Brief (Assumptions) / Trung bình |
| A-03 | PRD gốc viết tỷ giá theo cách ghi số Việt Nam (26.054 là 26,054 VND cho 1 USD; 18,95 là 18.95 VND cho 1 KRW). Pack viết mọi ví dụ theo cách ghi số của UI EN. | BR-13 đến BR-21, BR-39, BR-42, BR-44, BR-45, BR-52 đến BR-55 | Brief (Assumptions) / Cao |
| A-04 | Phần kỹ thuật của PRD gốc (cấu hình định dạng số, cách xác định ngôn ngữ và tiền tệ viết theo kiểu lập trình (CR-13), dữ liệu của báo giá và đơn, lệnh làm mới tỷ giá của công cụ, mã lỗi khi trùng quy tắc, cấu trúc bản dịch và danh sách key, dữ liệu doanh thu cho phân tích) chuyển sang tài liệu Technical design của Dev và tracking plan của Data. | Q-02 đến Q-12 | Brief (Assumptions) / Cao |
| A-05 | US-19 gốc có actor là dịch vụ lấy tỷ giá; đổi sang người hưởng lợi là nhân viên vận hành tỷ giá theo chuẩn user story. | US-19, JTBD-09 | Brief (Assumptions) / Cao |
| A-06 | Story gợi ý nhập tên Latin được tách từ BR-N13 vì PRD gốc chưa có US cho nội dung này. | US-23, MSG-16, MSG-17, DEP-10 | Brief (Assumptions) / Cao |
| A-07 | Hoá đơn VAT và báo cáo doanh thu giữ như hiện tại, không thêm tiền tệ nào khác. | BR-03, BR-04, DEP-07, US-18 | Brief (Assumptions) / Cao |
| A-08 | Danh sách ngôn ngữ, tiền tệ được bật phụ thuộc cấu hình của BU; các ngôn ngữ, tiền tệ trong rule là giá trị mẫu. | BR-22, BR-23, BR-25, BR-27, BR-29, BR-30, DEP-14 | Brief (Assumptions), quyết định 2 / Cao |
| A-09 | Định nghĩa, baseline và owner của các chỉ số do pipeline đề xuất theo yêu cầu của user ("tự xử lý"). | SM-01 đến SM-05 | Brief (Assumptions), quyết định 1 / Trung bình |
| A-10 | Lúc ra mắt, chế độ thứ bậc hiển thị là VND làm số chính trên mọi bề mặt; chế độ theo nhóm Browse/Pay bật được bằng cấu hình sau này. | BR-06, BR-05, BR-20 | Brief (Assumptions), quyết định 5 / Cao |
| A-11 | "Đơn vị làm tròn" của quy tắc tỷ giá làm tròn tỷ giá theo quy tắc (VND cho 1 đơn vị ngoại tệ). Ví dụ THB của PRD gốc ghi 787,88, khác kết quả làm tròn half-up 787.89; Pack dùng 787.89. | BR-52 | Brief (Assumptions) / Trung bình |
| A-12 | Cách xử lý dữ liệu cũ lúc ra mắt, checkout đang dở lúc ra mắt, khi tắt tính năng, khi tắt một ngôn ngữ hoặc tiền tệ, khi lấy tỷ giá mới không thành công trong checkout, và việc đơn chỉ lưu số tham khảo khi màn thanh toán đã hiển thị nó, do pipeline đề xuất theo yêu cầu của user ("tự đề xuất"); cần PO duyệt. | BR-43, BR-61, BR-62, BR-63, BR-64, BR-68 | Brief (Assumptions, đề xuất), quyết định 7, 9 / Thấp, chờ duyệt |
| A-13 | Các bề mặt CMS, coupon/campaign, landing page, trip card, payment promotion nằm ngoài phạm vi đợt này vì chưa có estimate; user chưa chắc chắn. | BR-05, SCR-01 đến SCR-11 | Brief (Assumptions), quyết định 4 / Trung bình |
| A-14 | Copy toast làm mới tỷ giá giữ nguyên như PRD gốc, kể cả chữ "bank". | MSG-12 | Brief (Assumptions), quyết định 7 / Cao |
| A-15 | Trong khi Legal chưa kết luận cho trang thanh toán, email xác nhận, My bookings và số tiền hoàn, bốn bề mặt này chỉ hiển thị VND. | BR-65, CB-05, DEP-03, SCR-07 đến SCR-10 | Pack đề xuất / Thấp, chờ duyệt |
| A-16 | JTBD-05 (người chia sẻ link) và JTBD-07 (kế toán) được suy ra từ US-09 và US-18; JTBD-08 (PO) và JTBD-09 (nhân viên vận hành tỷ giá) được tách từ một JTBD candidate chung vì tình huống và kết quả mong muốn khác nhau. | JTBD-05, JTBD-07, JTBD-08, JTBD-09 | Pack đề xuất / Trung bình |
| A-17 | Priority của các story do Pack đề xuất; PRD gốc không có priority. US-23 là Should vì không chặn ra mắt (quyết định 11). | US-01 đến US-23 | Pack đề xuất / Trung bình |
| A-18 | Copy của picker tiền tệ (MSG-04, MSG-05) do Pack đề xuất vì input chỉ nêu ý; copy lỗi nhập liệu trên form quy tắc tỷ giá (MSG-21) do Pack đề xuất vì input không có copy; thông báo lỗi tên hành khách (MSG-17) dùng copy hiện có của hệ thống. | MSG-04, MSG-05, MSG-17, MSG-21 | Pack đề xuất / Trung bình |
| A-19 | Mức lệch của tỷ giá mới so với biến động tối đa/ngày tính theo phần trăm so với tỷ giá hiện hành của cặp. | BR-54 | Pack đề xuất / Trung bình |
| A-20 | Hộp Payment Notice bản đầy đủ (MSG-08) ở checkout và Payment Notice rút gọn (MSG-09) ở màn thanh toán chỉ hiện khi màn đó đang hiển thị số tham khảo. Khi màn chỉ hiển thị VND (CB-02, CB-03, CB-04, BR-65), hai thông báo này không hiện, vì nội dung của chúng nói về số tham khảo và tiền tệ tham khảo. Việc MSG-07, MSG-10, MSG-11 có hiện khi tính năng tắt hay không thuộc Q-15. | US-13, MSG-08, MSG-09 | Pack đề xuất / Trung bình, chờ duyệt |

**Open Questions**

| ID | Question | Affects | Owner / Next Step |
|----|----------|---------|-------------------|
| Q-01 | Mức target cụ thể của tỷ lệ hoàn thành đơn và conversion UI ngoại ngữ là bao nhiêu? | SM-01, SM-02 | PO: chốt sau khi đo baseline 4 tuần trước khi bật cho Bus |
| Q-02 | Làm sao bảo đảm mọi số tiền trên web và app đi qua cùng một cách định dạng số (số lẻ, làm tròn, mã ISO, vị trí mã tiền), không còn chỗ nào tự định dạng riêng? | BR-09, BR-10, BR-11, BR-12, NFR-03, US-01 | Dev / Tech Lead: ghi trong Technical design |
| Q-03 | Làm sao đổi tiền tệ ở trang kết quả tìm kiếm mà không tải lại trang và không phải lấy lại kết quả tìm kiếm, để đạt NFR-01? | NFR-01, US-06, US-10 | Dev / Tech Lead: ghi trong Technical design |
| Q-04 | Lựa chọn ngôn ngữ, tiền tệ được lưu trên thiết bị và trên hồ sơ, đồng bộ khi đăng nhập như thế nào? | BR-31, BR-32, BR-33, US-07, US-08 | Dev / Tech Lead: ghi trong Technical design |
| Q-05 | Báo giá giữ cố định số VND, bảng tỷ giá, mốc hết hiệu lực tỷ giá và mốc hết giữ chỗ như thế nào, và tự chuyển sang bảng mới ra sao? | BR-39, BR-66, BR-67, BR-68, BR-69, BR-70, US-13, US-14 | Dev / Tech Lead: ghi trong Technical design |
| Q-06 | Số tham khảo được tính lại khi lưu đơn và lưu cùng đơn, cùng bản ghi hoàn tiền như thế nào để đạt NFR-03? | BR-42, BR-44, BR-45, BR-70, NFR-03, US-15, US-16 | Dev / Tech Lead: ghi trong Technical design |
| Q-07 | Công cụ tìm kiếm nhận các đường dẫn theo ngôn ngữ, danh sách trang của mỗi ngôn ngữ mới và trang mở bằng link có tham số như thế nào; bot được nhận diện ra sao để không bị tự nhận diện? | BR-28, BR-29, DEP-08, US-09 | Dev / Tech Lead cùng SEO |
| Q-08 | Luồng tạo bản dịch cho ngôn ngữ mới (tạo từ bản EN, xem trước trên web và app, đưa lên hệ thống ở trạng thái tắt, bật bằng cấu hình) có đúng không? Trang tạo và trang xem trước có cần không? | BR-35, SCR-18, SCR-19, US-20 | Dev / Tech Lead: xác nhận luồng đề xuất |
| Q-09 | Tỷ giá được làm mới ngay sau khi tạo, sửa quy tắc hoặc bấm làm mới trên công cụ như thế nào? | BR-48, US-22 | Dev / Tech Lead: ghi trong Technical design |
| Q-10 | Bật tắt, ramp theo vertical × platform và công tắc tắt khẩn cấp được vận hành ở đâu, bằng cách nào? | BR-60, BR-61, BR-72, BR-77, US-21 | Dev / Tech Lead: ghi trong Technical design |
| Q-11 | Dữ liệu doanh thu cho phân tích ghi số tiền và tiền thanh toán VND là bắt buộc, số tham khảo là thông tin phụ, như thế nào? | BR-04, US-18, SM-01 đến SM-05 | Data: ghi trong tracking plan |
| Q-12 | Search widget dùng lại được cho các ngôn ngữ thêm sau chỉ bằng cấu hình, không sửa code, như thế nào? | US-03, BR-35 | Dev / Tech Lead: ghi trong Technical design |
| Q-13 | MSG-08 viết số tham khảo dạng "~{số tham khảo} {mã tiền tệ}", trái với BR-12 (mã ngoại tệ đứng trước số). Giữ copy như input hay đổi thành "~{mã tiền tệ} {số tham khảo}"? | MSG-08, BR-12 | PO |
| Q-14 | Bảng tỷ giá chỉ hợp lệ khi có đủ tiền tệ chính của mọi ngôn ngữ đang bật (BR-49). Nếu vận hành tắt quy tắc tỷ giá của tiền tệ chính của một ngôn ngữ đang bật (ví dụ KRW của KO), mọi bảng mới sẽ không hợp lệ và sau N lần mọi bề mặt chỉ hiển thị VND (BR-56, BR-75). Điều tương tự xảy ra khi bật một ngôn ngữ mà tiền tệ chính chưa có quy tắc tỷ giá đang bật (BR-22, US-20). Đó có phải hành vi mong muốn, hay cần chặn việc tắt quy tắc (hoặc việc bật ngôn ngữ), hoặc đổi tiền tệ chính trước? | BR-22, BR-49, BR-53, BR-56, BR-75, US-20, US-22 | PO |
| Q-15 | Khi Currency Switch tắt cho một vertical × platform, picker tiền tệ có ẩn không, picker ngôn ngữ và UI ngoại ngữ có bị ảnh hưởng không, và khách có thấy thông báo nào không, kể cả MSG-07, MSG-10, MSG-11 ở checkout và màn thanh toán? Back office đơn hàng (SCR-15) có tiếp tục hiển thị thông tin tiền tệ đã lưu của đơn trong lúc tắt không (US-17 hiện giả định là có)? | BR-61, CB-03, MSG-07, MSG-10, MSG-11, US-05, US-06, US-13, US-17, US-21 | PO |
| Q-16 | "Mọi giá trong một phiên dùng cùng một bảng tỷ giá" (BR-48): khi phiên kéo dài qua một lần cập nhật 2 giờ, giá ngoài checkout chuyển sang bảng mới lúc nào? | BR-48, NFR-03, US-19 | PO cùng Dev / Tech Lead |
| Q-17 | Khi tiền tệ khách đang dùng không còn trong bảng tỷ giá (quy tắc bị tắt, BR-53), chỉ hiển thị VND kèm MSG-06 như US-06 gốc, hay chuyển sang ứng viên tiền tệ kế tiếp như BR-26 và BR-64? | BR-23, BR-26, BR-53, BR-64, CB-02 | PO |
| Q-18 | Ngôn ngữ chỉ khai báo một tiền tệ thì picker tiền tệ ở dạng chỉ đọc và hiển thị MSG-03 (US-06-AC7), nhưng danh sách tiền tệ khách chọn được luôn có VND (BR-23). Với ngôn ngữ như vậy, khách có chọn được VND không (picker không chỉ đọc), hay picker chỉ đọc và khách chỉ xem giá bằng tiền tệ duy nhất của ngôn ngữ? | BR-23, MSG-03, US-06 | PO |
| Q-19 | Khách mới mở link có chỉ định ngôn ngữ: tự nhận diện lấy ngôn ngữ trên link (BR-29) và kết quả tự nhận diện được lưu là giá trị không chủ động (BR-31), trong khi tham số trên link không được lưu vào thiết bị hay hồ sơ (BR-31). Ở phiên sau, khách này mở bằng ngôn ngữ của link (lưu là giá trị tự nhận diện), hay bằng ngôn ngữ tự nhận diện từ đường dẫn và trình duyệt, bỏ qua tham số trên link? | BR-29, BR-31, US-08, US-09 | PO |
| Q-20 | Bộ lọc và thanh trượt giá thuộc phạm vi hiển thị kép (BR-05), và không bề mặt nào được hiện ngoại tệ mà thiếu VND (BR-07). Trong khi đó khách chọn giá trị biên bằng tiền tệ tham khảo (BR-21), và lúc ra mắt VND là số chính (BR-06). Giá trị biên trên bộ lọc và thanh trượt chỉ hiển thị số tham khảo dạng xấp xỉ "~" như PRD gốc, hay kèm số VND tương ứng? Nếu kèm VND thì số đó là biên VND đã nới theo BR-21, hay là giá trị biên nhân tỷ giá? | BR-05, BR-06, BR-07, BR-21, US-12 | PO cùng Design (DEP-04) |
| Q-21 | Khi khách đang lọc theo khoảng giá (BR-21) mà đổi tiền tệ tham khảo ở trang kết quả tìm kiếm, bộ lọc giữ khoảng giá đã chọn và hiển thị lại bằng tiền tệ mới, hay đặt lại về toàn bộ khoảng giá? | BR-21, US-12 | PO |
| Q-22 | Dòng MSG-07 ở checkout, nhãn nút thanh toán MSG-10 và dòng MSG-11 dưới nút thanh toán có hiện trên UI VI không, hay chỉ trên UI ngoại ngữ? PRD gốc chỉ ghi nhãn nút "theo ngôn ngữ UI"; đổi copy ở checkout và màn thanh toán trên UI VI có thể ảnh hưởng SM-03. | US-13, MSG-07, MSG-10, MSG-11, SM-03 | PO |
| Q-23 | Số tham khảo đã lưu trên đơn (BR-44, BR-45, BR-70) có bị ẩn trên email xác nhận, My bookings, thông tin hoàn tiền và back office đơn hàng trong hai trường hợp sau không: (1) bảng tỷ giá hiện hành đang Cũ (BR-75, CB-02); (2) khách đang dùng VND trên UI ngoại ngữ (BR-08, CB-04)? BR-75 và BR-08 nói mọi bề mặt chỉ hiển thị VND, trong khi BR-44 giữ số tham khảo lúc đặt vĩnh viễn và chỉ có ngoại lệ khi xem trên UI VI. US-15, US-16, US-17 hiện đọc theo BR-44, BR-45: số đã lưu vẫn hiển thị. | BR-08, BR-44, BR-45, BR-75, CB-02, CB-04, US-15, US-16, US-17 | PO |
| Q-24 | Trong khi Currency Switch bật cho một vertical × platform ở một tỷ lệ traffic (BR-60), một khách có luôn ở cùng một nhóm (thấy số tham khảo, hoặc thấy như CB-03) qua các trang, các phiên và sau khi đăng nhập không? | BR-60, CB-03, US-21 | PO |
| Q-25 | Khi một lần cập nhật không lấy được tỷ giá của một cặp từ mọi nguồn (BR-47), nhưng bảng mới vẫn hợp lệ vì cặp đó không phải tiền tệ chính của ngôn ngữ đang bật nào (BR-49): bảng mới bỏ cặp đó (khách đang dùng tiền tệ đó thấy như CB-02), hay giữ tỷ giá hiện hành của cặp như khi tỷ giá mới bị bỏ qua (BR-54)? Nếu giữ, giữ tới khi nào? | BR-47, BR-48, BR-49, BR-54, CB-02, US-19 | PO |
