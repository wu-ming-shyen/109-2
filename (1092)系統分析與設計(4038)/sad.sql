-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2021-07-08 10:05:35
-- 伺服器版本： 10.4.19-MariaDB
-- PHP 版本： 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `sad`
--

-- --------------------------------------------------------

--
-- 資料表結構 `animal`
--

CREATE TABLE `animal` (
  `id` int(11) NOT NULL,
  `genus` varchar(10) NOT NULL,
  `species` varchar(10) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `age` varchar(20) NOT NULL,
  `img` varchar(255) NOT NULL,
  `color` varchar(10) NOT NULL,
  `fromwhere` varchar(255) NOT NULL,
  `open` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL,
  `u_id` int(11) DEFAULT NULL,
  `s_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `animal`
--

INSERT INTO `animal` (`id`, `genus`, `species`, `sex`, `age`, `img`, `color`, `fromwhere`, `open`, `status`, `u_id`, `s_id`) VALUES
(1, '貓', '混種貓', '母', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/838e227b-01f3-49a0-9d30-f20eb99dce6e_org.jpg', '', '', '', '', NULL, 16),
(2, '貓', '金吉拉', '母', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/8133e2df-15dc-406e-8a01-73958d4e7a66_org.jpg', '', '', '', '', NULL, 19),
(3, '貓', '加菲貓', '公', '', 'https://cdn.hk01.com/di/media/images/1167174/org/55fb71ee9cc97f0f9c468fbad2a96aa2.jpg/RpYGH6UotH0E4u80GKlahnUarIJsDUTE4Dkvn-A5L58', '', '', '', '', NULL, 11),
(4, '貓', '波斯貓', '母', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/3cf5492d-5be5-4c61-94de-8eaf7937f3b8_org.jpg', '', '', '', '', NULL, 11),
(5, '貓', '英國短毛貓', '母', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/cdd9ee2f-7f53-41ec-85ca-e23f094e0816_org.jpg', '', '', '', '', NULL, 11),
(6, '犬', '混種狗', '母', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/eb2dbe83-637f-4a5d-804d-5b2e647b7eff_org.jpg', '', '', '', '', NULL, 16),
(7, '犬', '貴賓犬', '公', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/698d0326-37d9-4b37-8d9b-2466e19a4571_org.jpg', '', '', '', '', NULL, 2),
(8, '犬', '米格魯', '公', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/f56ed796-94f8-497b-9878-cd063b79f6cd_org.JPG', '', '', '', '', NULL, 10),
(9, '犬', '吉娃娃', '公', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/13270b55-ad00-424e-8c11-be53ae31282d_org.JPG', '', '', '', '', NULL, 12),
(10, '犬', '英國鬥牛犬', '公', '', 'https://asms.coa.gov.tw/Amlapp/Upload/Pic/dfd4e9ae-3ce3-4068-ac29-ceb20d603afa_org.jpg', '', '', '', '', NULL, 16);

-- --------------------------------------------------------

--
-- 資料表結構 `contain`
--

CREATE TABLE `contain` (
  `s_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `time` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `contain`
--

INSERT INTO `contain` (`s_id`, `a_id`, `time`) VALUES
(16, 1, '2021-06-19'),
(16, 6, '2021-05-12'),
(16, 10, '2021-06-04'),
(11, 3, '2021-06-02'),
(11, 5, '2021-06-11'),
(11, 4, '2021-06-02');

-- --------------------------------------------------------

--
-- 資料表結構 `favorite`
--

CREATE TABLE `favorite` (
  `u_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `favorite`
--

INSERT INTO `favorite` (`u_id`, `a_id`) VALUES
(2, 3),
(2, 4);

-- --------------------------------------------------------

--
-- 資料表結構 `manager`
--

CREATE TABLE `manager` (
  `id` int(11) NOT NULL,
  `name` varchar(10) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `birthday` date NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `id_number` varchar(10) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `manager`
--

INSERT INTO `manager` (`id`, `name`, `email`, `password`, `birthday`, `Phone`, `id_number`, `sex`, `address`) VALUES
(1, 'A', 'B10856012@gmail.com', 'B10856012', '2021-06-13', '', '', '', ''),
(2, 'B', 'B10856021@gmail.com', 'B10856021', '2021-06-13', '', '', '', ''),
(3, 'C', 'B10856022@gmail.com', 'B10856022', '2021-06-13', '', '', '', ''),
(4, 'D', 'B10856034@gmail.com', 'B10856034', '2021-06-13', '', '', '', ''),
(5, 'E', 'B10856050@gmail.com', 'B10856050', '2021-06-13', '', '', '', ''),
(6, 'F', 'B10856055@gmail.com', 'B10856055', '2021-06-13', '', '', '', ''),
(7, 'G', 'michell10856012@gmail.com', 'michell891012', '2000-10-12', '090000000', 'A000000000', 'male', '912屏東縣內埔鄉學府路1號');

-- --------------------------------------------------------

--
-- 資料表結構 `requisition`
--

CREATE TABLE `requisition` (
  `r_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `squaremeters` int(11) NOT NULL,
  `havinganimals` int(11) NOT NULL,
  `salary` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `audit` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `requisition`
--

INSERT INTO `requisition` (`r_id`, `u_id`, `a_id`, `date`, `squaremeters`, `havinganimals`, `salary`, `address`, `audit`) VALUES
(1, 1, 1, '0000-00-00 00:00:00', 100, 0, 100000, '2', 'Yes'),
(2, 2, 2, '0000-00-00 00:00:00', 100, 0, 50000, '2', 'Yes'),
(3, 3, 3, '0000-00-00 00:00:00', 140, 1, 120000, '912屏東縣內埔鄉學府路1號', 'Yes'),
(4, 1, 3, '2021-06-14 16:00:00', 10, 0, 28000, '0', 'Yes'),
(5, 1, 3, '2021-06-14 18:28:44', 10, 0, 28000, '0', ''),
(8, 1, 3, '0000-00-00 00:00:00', 100, 1, 5000000, '台南', ''),
(9, 1, 3, '2021-06-15 17:19:59', 100, 0, 29000, '0', ''),
(10, 1, 3, '0000-00-00 00:00:00', 100, 1, 5000000, '台南', ''),
(11, 1, 3, '2021-06-15 17:24:36', 100, 1, 5000000, '台南', ''),
(12, 1, 4, '2021-06-15 17:24:57', 100, 1, 5000000, '台南', '');

-- --------------------------------------------------------

--
-- 資料表結構 `shelter`
--

CREATE TABLE `shelter` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` char(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `area` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `shelter`
--

INSERT INTO `shelter` (`id`, `name`, `email`, `password`, `phone`, `address`, `area`) VALUES
(1, '新北市政府動物保護防疫處', 'xinbei01@gmail.com', 'xinbei01', '0229596353', '新北市板橋區四川路一段157巷2號', '北部'),
(2, '新北市板橋區公立動物之家', 'xinbei02@gmail.com', 'xinbei02', '0289662158', '新北市板橋區板城路28-1號', '北部'),
(3, '新北市新店區公立動物之家', 'xinbei03@gmail.com', 'xinbei03', '0222159462', '新北市新店區安泰路235號', '北部'),
(4, '新北市中和區公立動物之家', 'xinbei04@gmail.com', 'xinbei04', '0286685547', '新北市中和區興南路三段100號', '北部'),
(5, '新北市淡水區公立動物之家', 'xinbei05@gmail.com', 'xinbei05', '0226267558', '新北市淡水區下圭柔山91之3號', '北部'),
(6, '新北市瑞芳區公立動物之家', 'xinbei06@gmail.com', 'xinbei06', '0224063481', '新北市瑞芳區靜安路四段(106縣道74.5K清潔隊場區內)', '北部'),
(7, '新北市五股區公立動物之家', 'xinbei07@gmail.com', 'xinbei07', '0282925265', '新北市五股區外寮路9-9號', '北部'),
(8, '新北市八里區公立動物之家', 'xinbei08@gmail.com', 'xinbei08', '0226194428', '新北市八里區長坑里6鄰長坑道路36號', '北部'),
(9, '新北市三芝區公立動物之家', 'xinbei09@gmail.com', 'xinbei09', '0226365436', '新北市三芝區青山路(龍巖人本旁)', '北部'),
(10, '臺北市動物之家', 'taipei01@gmail.com', 'taipei01', '0287913254', '臺北市內湖區潭美街852號', '北部'),
(11, '臺中市動物之家南屯園區', 'taichung01@gmail.com', 'taichung01', '0423850976', '臺中市南屯區中台路601號', '中部'),
(12, '臺南市動物之家灣裡站', 'tainan01@gmail.com', 'tainan01', '062964439', '臺南市南區省躬里14鄰萬年路580巷92號', '南部'),
(13, '臺南市動物之家善化站', 'tainan02@gmail.com', 'tainan02', '065832399', '臺南市善化區東昌里東勢寮1~19號', '南部'),
(14, '高雄市壽山動物保護教育園區', 'kaohsiung01@gmail.com', 'kaohsiung01', '075519059', '高雄市鼓山區萬壽路350號', '南部'),
(15, '高雄市燕巢動物保護關愛園區', 'kaohsiung02@gmail.com', 'kaohsiung02', '076051002', '高雄市燕巢區師大路98號', '南部'),
(16, '桃園市動物保護教育園區', 'Rehito1012@gmail.com', 'Meteor1012', '034861760', '桃園市新屋區永興里3鄰藻礁路1668號', '北部'),
(17, '宜蘭縣流浪動物中途之家', ' yilan01@gmail.com', 'yilan01', '039602350', '宜蘭縣五結鄉成興村利寶路60號', '北部'),
(18, '新竹縣公立動物收容所', ' hsinchu01@gmail.com', 'hsinchu01', '035519548', '新竹縣竹北市縣政五街192號', '北部'),
(19, '苗栗縣生態保育教育中心(動物收容所)', ' miaoli01@gmail.com', 'miaoli01', '037558228', '苗栗縣銅鑼鄉朝陽村6鄰朝北55-1號', '中部'),
(20, '彰化縣流浪狗中途之家', 'changhua01@gmail.com', 'changhua01', '048590638', '彰化縣員林市大峰里阿寶巷426號', '中部'),
(21, '南投縣公立動物收容所', 'nantou01@gmail.com', 'nantou01', '0492225440', '南投縣南投市嶺興路36-1號', '中部'),
(22, '雲林縣流浪動物收容所', 'yunlin01@gmail.com', 'yunlin01', '055523300', '雲林縣斗六市雲林路二段517號', '中部'),
(23, '嘉義縣流浪犬中途之家', 'chiayi01@gmail.com', 'chiayi01', '052950053', '嘉義縣大林鎮中坑里中興2-6號', '南部'),
(24, '屏東縣公立犬貓中途之家', ' pingtung01@gmail.com', 'pingtung01', '0905981077', '屏東縣內埔鄉學府路1號(屏東科技大學內)', '南部'),
(25, '臺東縣動物收容中心', 'taitung01@gmail.com', 'taitung01', '089362011', '臺東縣臺東市中華路4段999巷600號', '東部'),
(26, '花蓮縣流浪犬中途之家', '', '', '038421452', '花蓮縣吉安鄉南濱路1段599號', '東部'),
(27, '澎湖縣流浪動物收容中心', '', '', '069213559', '澎湖縣馬公市烏崁里260、261號', '離島'),
(28, '基隆市寵物銀行', '', '', '0224560148', '基隆市七堵區大華三路45-12號(欣欣安樂園旁)', '北部'),
(29, '新竹市動物保護教育園區', '', '', '035368329', '新竹市南寮里海濱路250號', '北部'),
(30, '嘉義市動物保護教育園區', '', '', '052168661', '嘉義市彌陀路31號旁', '南部'),
(31, '金門縣動物收容中心', '', '', '082336625', '金門縣金湖鎮裕民農莊20號', '離島'),
(32, '連江縣流浪犬收容中心', '', '', '083625003', '連江縣南竿鄉復興村223號', '離島');

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(10) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `id_number` char(10) NOT NULL,
  `phone` char(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `birthday` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `sex`, `id_number`, `phone`, `address`, `birthday`) VALUES
(1, '吳明軒', 'B10856012@mail.npust.edu.tw', 'B10856012', '男性', 'D000000012', '091892873', '台南市東區長榮路二段24巷130號', '2000-10-12'),
(2, '吳冠儀', 'B10856021@mail.npust.edu.tw', 'B10856021', 'female', 'D000000021', '0900000021', '912屏東縣內埔鄉學府路1號', '2001-07-31'),
(3, '林暐竣', 'B10856022@mail.npust.edu.tw', 'B10856022', 'male', 'D000000022', '0900000022', '912屏東縣內埔鄉學府路1號', '2000-10-02'),
(4, '吳書婷', 'B10856034@mail.npust.edu.tw', 'B10856034', 'female', 'D000000034', '0900000034', '912屏東縣內埔鄉學府路1號', '2001-03-08'),
(5, '蔡承恩', 'B10856050@mail.npust.edu.tw', 'B10856050', 'male', 'D000000050', '0900000050', '912屏東縣內埔鄉學府路1號', '2001-04-30'),
(6, '吳雲聖', 'B10856055@mail.npust.edu.tw', 'B10856055', 'male', 'D000000055', '0900000055', '912屏東縣內埔鄉學府路1號', '2000-12-12');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `animal`
--
ALTER TABLE `animal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `animal_of_user` (`u_id`),
  ADD KEY `animal_of_shelter` (`s_id`);

--
-- 資料表索引 `contain`
--
ALTER TABLE `contain`
  ADD KEY `contain_ibfk_1` (`a_id`),
  ADD KEY `contain_ibfk_2` (`s_id`);

--
-- 資料表索引 `favorite`
--
ALTER TABLE `favorite`
  ADD KEY `favorite_animal` (`a_id`),
  ADD KEY `favorite_user` (`u_id`);

--
-- 資料表索引 `manager`
--
ALTER TABLE `manager`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `requisition`
--
ALTER TABLE `requisition`
  ADD PRIMARY KEY (`r_id`),
  ADD KEY `requisition_ibfk_1` (`u_id`),
  ADD KEY `a_id` (`a_id`);

--
-- 資料表索引 `shelter`
--
ALTER TABLE `shelter`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `animal`
--
ALTER TABLE `animal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `manager`
--
ALTER TABLE `manager`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `requisition`
--
ALTER TABLE `requisition`
  MODIFY `r_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `shelter`
--
ALTER TABLE `shelter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `animal`
--
ALTER TABLE `animal`
  ADD CONSTRAINT `animal_of_shelter` FOREIGN KEY (`s_id`) REFERENCES `shelter` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `animal_of_user` FOREIGN KEY (`u_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `contain`
--
ALTER TABLE `contain`
  ADD CONSTRAINT `contain_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `animal` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `contain_ibfk_2` FOREIGN KEY (`s_id`) REFERENCES `shelter` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `favorite`
--
ALTER TABLE `favorite`
  ADD CONSTRAINT `favorite_animal` FOREIGN KEY (`a_id`) REFERENCES `animal` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `favorite_user` FOREIGN KEY (`u_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `requisition`
--
ALTER TABLE `requisition`
  ADD CONSTRAINT `requisition_ibfk_1` FOREIGN KEY (`u_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `requisition_ibfk_2` FOREIGN KEY (`a_id`) REFERENCES `animal` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
