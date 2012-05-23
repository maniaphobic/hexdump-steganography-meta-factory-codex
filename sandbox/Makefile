#
#
#

CONVERT_SPLIT_TO_ZETA		= ./convert-split-to-zeta
HDF_MEMO_KEY			= key.txt
HDF_MEMO_PLAIN			= hdf-memo.txt
HDF_MEMO_ENCRYPTED		= data/hdf-memo/encrypted/hdf-memo,xor,b64.txt
HDF_MEMO_ENCRYPTED_SPLIT	= data/hdf-memo/encrypted/split
HDF_MEMO_ENCRYPTED_ZETA		= data/hdf-memo/encrypted/zeta
MEMO_SPLITTER			= ./split-memo
MEMO_ENCRYPTER			= ./cryptxor.py
REPO_PATH			= elip001:/local/www/site01/content/hexdump
SPLIT_PREFIX			= hdf_

#
#
#

all: encrypt-memo split-encrypted-memo convert-split-to-zeta

$(HDF_MEMO_ENCRYPTED): $(HDF_MEMO_KEY) $(HDF_MEMO_PLAIN)
	$(MEMO_ENCRYPTER) $(HDF_MEMO_KEY) $(HDF_MEMO_PLAIN) $(HDF_MEMO_ENCRYPTED)

convert-split-to-zeta zetafy: $(HDF_MEMO_ENCRYPTED_SPLIT)
	$(CONVERT_SPLIT_TO_ZETA) $(HDF_MEMO_ENCRYPTED_SPLIT) $(HDF_MEMO_ENCRYPTED_ZETA)

ExampleScalaGet: ExampleScalaGet.class

ExampleScalaGet.class: ExampleScalaGet.scala
	scalac $<

encrypt encrypt-memo: $(HDF_MEMO_ENCRYPTED)

PhaseTwo: PhaseTwo.class

PhaseTwo.class: phase2.scala
	scalac $<

split split-encrypted-memo: $(HDF_MEMO_ENCRYPTED)
	$(MEMO_SPLITTER) $(HDF_MEMO_ENCRYPTED) $(HDF_MEMO_ENCRYPTED_SPLIT) $(SPLIT_PREFIX)

upload upload-zeta:
	rsync -av $(HDF_MEMO_ENCRYPTED_ZETA)/ $(REPO_PATH)

clean:
	rm $(HDF_MEMO_ENCRYPTED) $(HDF_MEMO_ENCRYPTED_SPLIT)/* $(HDF_MEMO_ENCRYPTED_ZETA)/*

