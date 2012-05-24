#
#
#

BIN_DIR				= bin
CONFIG_DIR			= config

CONVERT_SPLIT_TO_ZETA		= $(BIN_DIR)/convert-split-to-zeta
HDF_MEMO_KEY			= $(CONFIG_DIR)/xor-key.txt
HDF_MEMO_PLAIN			= $(CONFIG_DIR)/hdf-memo.txt
HDF_MEMO_ENCRYPTED		= data/hdf-memo/encrypted/hdf-memo,xor,b64.txt
HDF_MEMO_ENCRYPTED_SPLIT	= data/hdf-memo/encrypted/split
HDF_MEMO_ENCRYPTED_ZETA		= data/hdf-memo/encrypted/zeta
MEMO_SPLITTER			= $(BIN_DIR)/split-memo
MEMO_ENCRYPTER			= $(BIN_DIR)/cryptxor
REPO_PATH			= elip001:/local/www/site01/content/hexdump
SPLIT_PREFIX			= hdf_

#
#
#

all: encrypt-memo split-encrypted-memo convert-split-to-zeta

$(HDF_MEMO_ENCRYPTED): $(HDF_MEMO_KEY) $(HDF_MEMO_PLAIN)
	$(MEMO_ENCRYPTER) $(HDF_MEMO_KEY) $(HDF_MEMO_PLAIN) $(HDF_MEMO_ENCRYPTED)

$(HDF_MEMO_KEY):

$(HDF_MEMO_PLAIN):

convert-split-to-zeta zetafy: $(HDF_MEMO_ENCRYPTED_SPLIT)
	$(CONVERT_SPLIT_TO_ZETA) $(HDF_MEMO_ENCRYPTED_SPLIT) $(HDF_MEMO_ENCRYPTED_ZETA)

encrypt encrypt-memo: $(HDF_MEMO_ENCRYPTED)

split split-encrypted-memo: $(HDF_MEMO_ENCRYPTED)
	$(MEMO_SPLITTER) $(HDF_MEMO_ENCRYPTED) $(HDF_MEMO_ENCRYPTED_SPLIT) $(SPLIT_PREFIX)

upload upload-zeta:
	rsync -av $(HDF_MEMO_ENCRYPTED_ZETA)/ $(REPO_PATH)

clean:
	rm $(HDF_MEMO_ENCRYPTED) $(HDF_MEMO_ENCRYPTED_SPLIT)/* $(HDF_MEMO_ENCRYPTED_ZETA)/*

